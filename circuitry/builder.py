import logging
import math
import operator

from circuitry import error_listener
from circuitry.component import Component
from circuitry.gen.CircuitryParser import CircuitryParser
from circuitry.gen.CircuitryParserVisitor import CircuitryParserVisitor
from circuitry.stdlib.math import internal_builtins
from circuitry.utils import engineering_str_to_float

logger = logging.getLogger(__name__)


class CircuitBuilderVisitor(CircuitryParserVisitor):
    def __init__(self, error_listener):
        # wartości
        self.scopes = [{'pi': math.pi}]
        # śledzenie definicji/wykorzystania dla warningów
        self.symbols = [{}]
        self.error_listener = error_listener

        self.imports = []
        self.aliases = {}
        self.components = []
        self.functions = {}
        self.subcircuits = {}
        self.simulations = []

        self._arithmetic_ops = {
            '+': operator.add, '-': operator.sub,
            '*': operator.mul, '/': operator.truediv,
            '%': operator.mod, '^': operator.pow,
        }
        self._relational_ops = {
            '==': operator.eq, '!=': operator.ne,
            '<': operator.lt, '<=': operator.le,
            '>': operator.gt, '>=': operator.ge,
        }

    # ─────────────────── Scope Helpers ──────────────────────────
    def push_scope(self):
        self.scopes.append({})
        self.symbols.append({})

    def pop_scope(self):
        # przed zniszczeniem zakresu, wypisz warningi dla niewykorzystanych
        current = self.symbols[-1]
        for name, info in current.items():
            if not info["used"]:
                line, col = info["defined"]
                val = info["value"]
                self.error_listener.warning(
                    line, col,
                    f"Zmiennej '{name}' nigdy nie użyto. Wartość przypisana to {val!r}."
                )
        # usunięcie zakresu
        self.symbols.pop()
        self.scopes.pop()

    def current_scope(self):
        return self.scopes[-1]

    def assign(self, name, value, ctx=None):
        # 1) Rejestracja definicji i wartości w symbols
        top = self.symbols[-1]
        if name not in top:
            if ctx is not None:
                token = ctx.ID().getSymbol()
                defined_at = (token.line, token.column)
            else:
                defined_at = (0, 0)
            top[name] = {
                "defined": defined_at,
                "used": False,
                "value": value
            }
        else:
            # jeśli ponowna definicja, aktualizujemy tylko wartość
            top[name]["value"] = value

        # 2) Standardowe przypisanie wartości w self.scopes
        for scope in reversed(self.scopes):
            if name in scope:
                scope[name] = value
                return
        # jeśli nie istniało wcześniej, dodajemy do bieżącego zakresu
        self.current_scope()[name] = value

    def resolve(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return self.aliases.get(name, name)

    def _to_number(self, v):
        if isinstance(v, str):
            resolved = self.resolve(v)
            if not isinstance(resolved, str):
                v = resolved
            else:
                try:
                    return engineering_str_to_float(v)
                except ValueError:
                    raise TypeError(f"Cannot resolve or convert '{v}' to a number")
        if isinstance(v, (int, float)):
            return v
        raise TypeError(f"Cannot convert {v!r} to a number")

    # ─────────────────── Entry Point ────────────────────────────
    def visitProgram(self, ctx: CircuitryParser.ProgramContext):
        for imp in ctx.importStatement():
            self.visit(imp)
        for stmt in ctx.circuitStatement():
            self.visit(stmt)
        for stmt in ctx.measurementStatement():
            self.visit(stmt)
        for stmt in ctx.simulationStatement():
            self.visit(stmt)
        for stmt in ctx.drawingStatement():
            self.visit(stmt)

    # ─────────────────── Import ──────────────────────────────────
    def visitImportStatement(self, ctx):
        self.imports.extend(t.getText() for t in ctx.ID())

    # ─────────────────── Alias & Let ────────────────────────────
    def visitAliasStatement(self, ctx):
        for asn in ctx.aliasAssignment():
            name, target = self.visit(asn)
            self.aliases[name] = target

    def visitAliasAssignment(self, ctx):
        return ctx.ID(0).getText(), ctx.ID(1).getText()

    def visitLetStatement(self, ctx):
        for lasn in ctx.letAssignment():
            name, val = self.visit(lasn)

    def visitLetAssignment(self, ctx: CircuitryParser.LetAssignmentContext):
        name = ctx.ID().getText()
        val = self.visit(ctx.expr())

        # 1) przypisz i zarejestruj zmienną
        self.assign(name, val, ctx)

        # 2) wykryj stałe wyrażenie: bool, int, float lub string
        if isinstance(val, (bool, int, float, str)):
            token = ctx.ID().getSymbol()
            # dla stringów usuń np. cudzysłowy w wyświetleniu
            display_val = f'"{val}"' if isinstance(val, str) else val
            self.error_listener.warning(
                token.line,
                token.column,
                f"Wyrażenie dla '{name}' zawsze zwraca wartość {display_val}."
            )

        return name, val

    # ─────────────────── Assignment ──────────────────────────────
    def visitAssignmentStatement(self, ctx: CircuitryParser.AssignmentStatementContext):
        var = ctx.ID().getText()
        if ctx.unaryAssignmentOperator():
            op = ctx.unaryAssignmentOperator().getText()
            curr = self.resolve(var)
            new_val = curr + 1 if op == '++' else curr - 1
            self.assign(var, new_val, ctx)
        else:
            op = ctx.binaryAssignmentOperator().getText()
            val = self.visit(ctx.expr())
            if op == '=':
                # 1) przypisz z kontekstem
                self.assign(var, val, ctx)

                # 2) warning jeśli czysta stała
                if isinstance(val, (bool, int, float, str)):
                    token = ctx.ID().getSymbol()
                    display = f'"{val}"' if isinstance(val, str) else val
                    self.error_listener.warning(
                        token.line, token.column,
                        f"Przypisanie do '{var}' zawsze daje wartość {display}."
                    )
            else:
                curr = self.resolve(var)
                fn = self._arithmetic_ops[op[:-1]]
                new_val = fn(curr, val)
                self.assign(var, new_val, ctx)

    # ─────────────────── Expression Statement ───────────────────
    def visitExpressionStatement(self, ctx: CircuitryParser.ExpressionStatementContext):
        # Evaluate and discard
        self.visit(ctx.expr())

    # ─────────────────── Control Flow ────────────────────────────
    def visitBlock(self, ctx: CircuitryParser.BlockContext):
        self.push_scope()
        for stmt in ctx.circuitStatement():
            self.visit(stmt)
        self.pop_scope()

    def visitIfStatement(self, ctx: CircuitryParser.IfStatementContext):
        if self.visit(ctx.expr()):
            self.visit(ctx.block(0))
        elif ctx.ELSE():
            self.visit(ctx.block(1))

    def visitWhileStatement(self, ctx: CircuitryParser.WhileStatementContext):
        while self.visit(ctx.expr()):
            self.visit(ctx.block())

    def visitDoWhileStatement(self, ctx: CircuitryParser.DoWhileStatementContext):
        while True:
            self.visit(ctx.block())
            if not self.visit(ctx.expr()):
                break

    def visitForStatement(self, ctx: CircuitryParser.ForStatementContext):
        self.push_scope()
        if ctx.forInit():
            self.visit(ctx.forInit())
        # allow empty condition as true
        cond_ctx = ctx.expr()
        while (self.visit(cond_ctx) if cond_ctx else True):
            self.visit(ctx.block())
            if ctx.forUpdate():
                self.visit(ctx.forUpdate())
        self.pop_scope()

    # ─── forInit variants ─────────────────────────────────────────
    def visitForInitLet(self, ctx: CircuitryParser.ForInitLetContext):
        name, val = self.visit(ctx.letAssignment())
        self.assign(name, val)

    def visitForInitAssign(self, ctx: CircuitryParser.ForInitAssignContext):
        name, val = self.visit(ctx.letAssignment())
        self.assign(name, val)

    def visitForInitIncDec(self, ctx: CircuitryParser.ForInitIncDecContext):
        var = ctx.ID().getText();
        op = ctx.unaryAssignmentOperator().getText()
        curr = self.resolve(var)
        self.assign(var, curr + 1 if op == '++' else curr - 1)

    def visitForInitBinOp(self, ctx: CircuitryParser.ForInitBinOpContext):
        var = ctx.ID().getText();
        op = ctx.binaryAssignmentOperator().getText()
        val = self.visit(ctx.expr())
        if op == '=':
            self.assign(var, val)
        else:
            curr = self.resolve(var)
            fn = self._arithmetic_ops[op[:-1]]
            self.assign(var, fn(curr, val))

    # ─── forUpdate variants ──────────────────────────────────────
    def visitForUpdateIncDec(self, ctx: CircuitryParser.ForUpdateIncDecContext):
        self.visitForInitIncDec(ctx)

    def visitForUpdateBinOp(self, ctx: CircuitryParser.ForUpdateBinOpContext):
        self.visitForInitBinOp(ctx)

    def visitSwitchStatement(self, ctx: CircuitryParser.SwitchStatementContext):
        key = self.visit(ctx.expr())
        for case in ctx.caseStatement():
            if self.visit(case.expr()) == key:
                self.visit(case.block())
                return
        if ctx.defaultStatement():
            self.visit(ctx.defaultStatement().block())

    # ─────────────────── Components ───────────────────────────────
    def visitComponentStatement(self, ctx: CircuitryParser.ComponentStatementContext):
        ctype = ctx.componentType().getText()
        cname = ctx.ID().getText()
        val = self.visit(ctx.expr())
        nodes = [self.visit(n) for n in ctx.nodeList().nodeMapping()]
        self.components.append(Component(ctype, cname, val, nodes))

    def visitDirectNode(self, ctx: CircuitryParser.DirectNodeContext):
        return ctx.ID().getText()

    def visitRemappedNode(self, ctx: CircuitryParser.RemappedNodeContext):
        return (ctx.ID(0).getText(), ctx.ID(1).getText())

    def visitSubNode(self, ctx: CircuitryParser.SubNodeContext):
        base = ctx.ID().getText();
        suf = ''.join(d.getText() for d in ctx.dottedNode())
        return f"{base}{suf}"

    # ─── Series & Parallel ────────────────────────────────────────
    def visitSeriesStatement(self, ctx: CircuitryParser.SeriesStatementContext):
        nodes = [self.visit(n) for n in ctx.nodeList().nodeMapping()]
        elems = [self.visit(e) for e in ctx.seriesBody().seriesElement()]
        for _, ctype, cname, val, rev in elems:
            lst = list(reversed(nodes)) if rev else nodes
            self.components.append(Component(ctype, cname, val, lst))

    def visitParallelStatement(self, ctx: CircuitryParser.ParallelStatementContext):
        nodes = [self.visit(n) for n in ctx.nodeList().nodeMapping()]
        elems = [self.visit(e) for e in ctx.parallelBody().parallelElement()]
        for _, ctype, cname, val, rev in elems:
            lst = list(reversed(nodes)) if rev else nodes
            self.components.append(Component(ctype, cname, val, lst))

    def visitSeriesAssignment(self, ctx: CircuitryParser.SeriesAssignmentContext):
        return ("seriesElem",
                ctx.componentType().getText(),
                ctx.ID().getText(),
                self.visit(ctx.expr()),
                bool(ctx.REVERSED()))

    def visitParallelAssignment(self, ctx: CircuitryParser.ParallelAssignmentContext):
        return ("parallelElem",
                ctx.componentType().getText(),
                ctx.ID().getText(),
                self.visit(ctx.expr()),
                bool(ctx.REVERSED()))

    # ─── Functions & Subcircuits ─────────────────────────────────
    def visitFunctionDefinition(self, ctx: CircuitryParser.FunctionDefinitionContext):
        name = ctx.ID().getText()
        params = [p.ID().getText() for p in ctx.functionParams().functionParam()] if ctx.functionParams() else []
        self.functions[name] = (params, ctx.functionBlock())

    def visitFunctionBlock(self, ctx: CircuitryParser.FunctionBlockContext):
        self.push_scope()
        for child in ctx.children:
            # circuitStatement or returnStatement
            if hasattr(child, 'circuitStatement'):
                for stmt in child.circuitStatement():
                    self.visit(stmt)
            elif hasattr(child, 'RETURN'):
                res = self.visit(child)
                self.pop_scope()
                return res
        self.pop_scope()

    def visitReturnStatement(self, ctx: CircuitryParser.ReturnStatementContext):
        return self.visit(ctx.expr())

    def visitFuncCallExpr(self, ctx):
        name = ctx.functionCall().ID().getText()
        args = self.visitFunctionCallArgs(ctx.functionCall().functionCallArgs()) \
            if ctx.functionCall().functionCallArgs() else {}

        # Check internal built-ins first
        if name in internal_builtins:
            # Call internal built-in function with args
            res = internal_builtins[name](args)

            # If internal log, return None explicitly (already done)
            if name == "print":
                return None
            return res

        # User-defined function
        if name in self.functions:
            params, body = self.functions[name]
            self.push_scope()
            for p, v in zip(params, args.get('_pos', [])):
                self.assign(p, v)
            res = self.visitFunctionBlock(body)
            self.pop_scope()
            return res

        # Fallback: maybe just return args for now
        return args

    def visitSubcircuitDefinition(self, ctx: CircuitryParser.SubcircuitDefinitionContext):
        name = ctx.ID().getText()
        params = [p.ID().getText() for p in ctx.subcircuitParams().subcircuitParam()] if ctx.subcircuitParams() else []
        body = ctx.block().circuitStatement()
        self.functions[name] = (params, body)

    def visitFunctionCallArgs(self, ctx: CircuitryParser.FunctionCallArgsContext):
        d = {}
        for arg in ctx.functionCallArg():
            # keyword: ID ASSIGN expr
            if arg.getChildCount() == 3 and arg.getChild(1).getText() == '=':
                key = arg.getChild(0).getText()
                val = self.visit(arg.getChild(2))
                d[key] = val
            else:
                # positional: single child expr
                pos_val = self.visit(arg.getChild(0))
                d.setdefault('_pos', []).append(pos_val)
        return d

    # ─── Simulation & Measurement ────────────────────────────────
    def visitSimulationStatement(self, ctx: CircuitryParser.SimulationStatementContext):
        sim_type = ctx.simulationType().getText().upper()
        args = self.visitFunctionCallArgs(ctx.functionCallArgs()) if ctx.functionCallArgs() else {}

        self.simulations.append({
            'type': sim_type,
            'params': args['_pos'] if '_pos' in args else {},
        })

        logger.debug(f"Added simulation: {sim_type} with parameters {args}")

    def visitMeasurementStatement(self, ctx: CircuitryParser.MeasurementStatementContext):
        logger.debug("Measure %s", ctx.ID().getText())

    # ─── Drawing ──────────────────────────────────────────────────
    def visitDrawingStatement(self, ctx: CircuitryParser.DrawingStatementContext):
        name = ctx.ID().getText()
        x = engineering_str_to_float(ctx.FLOAT_LITERAL(0).getText())
        y = engineering_str_to_float(ctx.FLOAT_LITERAL(1).getText())
        logger.debug("Draw %s at (%.3g, %.3g)", name, x, y)

    # ─── Expressions ─────────────────────────────────────────────
    def visitFloatLiteralExpr(self, ctx):
        return engineering_str_to_float(ctx.FLOAT_LITERAL().getText())

    def visitStringLiteralExpr(self, ctx):
        return ctx.STRING_LITERAL().getText()[1:-1]

    def visitTrueLiteralExpr(self, ctx):
        return True

    def visitFalseLiteralExpr(self, ctx):
        return False

    def visitIdExpr(self, ctx):
        name = ctx.ID().getText()
        # oznacz, że użyto tej zmiennej
        for scope in reversed(self.symbols):
            if name in scope:
                scope[name]["used"] = True
                return self.resolve(name)
        
        # variable not declared, throw semantic error
        token = ctx.ID().getSymbol()
        self.error_listener.semanticError(
            token.line,
            token.column,
            f"Variable '{name}' is used but was never declared."
        )
        return None 

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitAddSubExpr(self, ctx):
        a = self._to_number(self.visit(ctx.expr(0)))
        b = self._to_number(self.visit(ctx.expr(1)))
        return self._arithmetic_ops[ctx.op.text](a, b)

    def visitMulDivExpr(self, ctx):
        a = self._to_number(self.visit(ctx.expr(0)))
        b = self._to_number(self.visit(ctx.expr(1)))
        return self._arithmetic_ops[ctx.op.text](a, b)

    def visitModExpr(self, ctx):
        a = self._to_number(self.visit(ctx.expr(0)))
        b = self._to_number(self.visit(ctx.expr(1)))
        return self._arithmetic_ops['%'](a, b)

    def visitExpExpr(self, ctx):
        a = self._to_number(self.visit(ctx.expr(0)))
        b = self._to_number(self.visit(ctx.expr(1)))
        return self._arithmetic_ops['^'](a, b)

    def visitRelationalExpr(self, ctx: CircuitryParser.RelationalExprContext):
        l = self._to_number(self.visit(ctx.expr(0)))
        r = self._to_number(self.visit(ctx.expr(1)))
        return self._relational_ops[ctx.op.text](l, r)

    def visitAndExpr(self, ctx):
        return bool(self.visit(ctx.expr(0))) and bool(self.visit(ctx.expr(1)))

    def visitOrExpr(self, ctx):
        return bool(self.visit(ctx.expr(0))) or bool(self.visit(ctx.expr(1)))

    def visitNotExpr(self, ctx):
        return not bool(self.visit(ctx.expr()))
