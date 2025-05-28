from antlr4 import ParseTreeWalker, TerminalNode
from circuitry.component import Component
from circuitry.evaluator import parse_value
from circuitry.gen.CircuitryParser import CircuitryParser
from circuitry.gen.CircuitryParserListener import CircuitryParserListener
import math

def text_of(node):
    return node if isinstance(node, str) else node.getText()

def get_id_text(mapping, index=0):
    if isinstance(mapping, str):
        return mapping
    ids = mapping.ID()
    if isinstance(ids, list):
        return text_of(ids[index])
    else:
        return text_of(ids)

class CircuitBuilder(CircuitryParserListener):
    def __init__(self):
        self.components   = []
        self.aliases      = {}
        self.variables    = {"pi": math.pi}
        self.builtins     = {
            "sqrt": math.sqrt,
            "sine": lambda **kwargs: {"type": "sine", **kwargs}
        }
        self.functions    = {}
        self._cond_stack  = [True]


    def _collecting(self):
        return all(self._cond_stack)

    # --- ALIAS ---
    def exitAliasStatement(self, ctx:CircuitryParser.AliasStatementContext):
        if not self._collecting(): return
        for aliasCtx in ctx.aliasAssignment():
            name = text_of(aliasCtx.ID())
            rhs  = aliasCtx.expr()
            if isinstance(rhs, CircuitryParser.IdExprContext):
                val = text_of(rhs)
            else:
                val = str(self.eval_expr(rhs))
            self.aliases[name] = val

    # --- LET ---
    def exitLetStatement(self, ctx:CircuitryParser.LetStatementContext):
        if not self._collecting(): return
        for letCtx in ctx.letAssignment():
            name = text_of(letCtx.ID())
            val  = self.eval_expr(letCtx.expr())
            self.variables[name] = val

    # --- COMPONENT ---
    def exitComponentStatement(self, ctx:CircuitryParser.ComponentStatementContext):
        if not self._collecting(): return
        ctype = text_of(ctx.componentType().ID())
        name  = text_of(ctx.ID())
        value = self.eval_expr(ctx.expr())
        nodes = []
        for mapping in ctx.nodeList().nodeMapping():
            kind = type(mapping).__name__
            if kind == "DirectNodeContext":
                nodes.append(get_id_text(mapping, 0))
            elif kind == "RemappedNodeContext":
                nodes.append(get_id_text(mapping, 1))
            elif kind == "SubNodeContext":
                nodes.append(text_of(mapping.getText()))
            else:
                raise ValueError(f"Unknown nodeMapping type: {kind}")
        self.components.append(Component(ctype, name, value, nodes))

    # --- ASSIGNMENT STATEMENTS ---
    def exitAssignmentStatement(self, ctx:CircuitryParser.AssignmentStatementContext):
        if not self._collecting(): return
        var = text_of(ctx.ID())
        if ctx.unaryAssignmentOperator():  # ++ or --
            op = ctx.unaryAssignmentOperator().getText()
            self.variables[var] = self.variables.get(var, 0) + (1 if op == '++' else -1)
        else:
            rhs = self.eval_expr(ctx.expr())
            self.variables[var] = rhs

    # --- FUNCTION DEFINITION ---
    def exitFunctionDefinition(self, ctx:CircuitryParser.FunctionDefinitionContext):
        if not self._collecting(): return
        fname  = text_of(ctx.ID())
        params = [
            text_of(p.ID())
            for p in (ctx.functionParams().functionParam() if ctx.functionParams() else [])
        ]
        body = ctx.functionBody().returnStatement().expr()
        self.functions[fname] = {"params": params, "body": body}

    # --- IF / ELSE STACKING ---
    def enterConditionWithBlock(self, ctx:CircuitryParser.ConditionWithBlockContext):
        cond = self.eval_bool(ctx.booleanExpr())
        self._cond_stack.append(cond)

    def exitConditionWithBlock(self, ctx:CircuitryParser.ConditionWithBlockContext):
        self._cond_stack.pop()

    def exitIfStatement(self, ctx:CircuitryParser.IfStatementContext):
        while len(self._cond_stack) > 1:
            self._cond_stack.pop()

    # --- FOR LOOP ---
    def exitForStatement(self, ctx: CircuitryParser.ForStatementContext):
        if not self._collecting():
            return

        # ———————————————————————————————————————————————
        # 1) pull out the two header assignments (i = …) if present
        # ———————————————————————————————————————————————
        assigns = ctx.getTypedRuleContexts(CircuitryParser.AssignmentStatementContext)
        initAssign   = assigns[0] if len(assigns) > 0 else None
        updateAssign = assigns[1] if len(assigns) > 1 else None

        if initAssign:
            self.exitAssignmentStatement(initAssign)

        cond_ctx   = ctx.booleanExpr()
        body_stmts = ctx.topologyStatement()

        # ———————————————————————————————————————————————
        # 2) loop
        # ———————————————————————————————————————————————
        while self.eval_bool(cond_ctx):
            for stmt in body_stmts:
                # manually dispatch the right exitXXX
                if stmt.aliasStatement():
                    self.exitAliasStatement(stmt.aliasStatement())
                elif stmt.letStatement():
                    self.exitLetStatement(stmt.letStatement())
                elif stmt.componentStatement():
                    self.exitComponentStatement(stmt.componentStatement())
                elif stmt.assignmentStatement():
                    self.exitAssignmentStatement(stmt.assignmentStatement())
                elif stmt.ifStatement():
                    self.exitIfStatement(stmt.ifStatement())
                # … and so on for seriesStatement, parallelStatement, etc.

            if updateAssign:
                self.exitAssignmentStatement(updateAssign)

    # --- BOOLEAN EVALUATION ---
    def eval_bool(self, bctx:CircuitryParser.BooleanExprContext) -> bool:
        if bctx.relationalOperator():
            l  = self.eval_expr(bctx.expr(0))
            r  = self.eval_expr(bctx.expr(1))
            op = text_of(bctx.relationalOperator())
            return {"==":l==r,"!=":l!=r,"<":l<r,">":l>r,"<=":l<=r,">=":l>=r}[op]
        if bctx.AND():
            return self.eval_expr(bctx.expr(0)) and self.eval_expr(bctx.expr(1))
        if bctx.OR():
            return self.eval_expr(bctx.expr(0)) or self.eval_expr(bctx.expr(1))
        if bctx.NOT():
            return not self.eval_expr(bctx.expr(0))
        return bool(self.eval_expr(bctx.expr(0)))

    # --- EXPRESSION EVALUATOR ---
    def eval_expr(self, ctx):
        # function calls
        if isinstance(ctx, CircuitryParser.FuncCallExprContext):
            fc      = ctx.functionCall()
            fname   = text_of(fc.ID())
            args_ctx = fc.functionCallArgs()
            if fname in self.builtins:
                fn, args, kwargs = self.builtins[fname], [], {}
                if args_ctx:
                    for ch in args_ctx.children:
                        if text_of(ch) == ',': continue
                        if isinstance(ch, CircuitryParser.FunctionCallPositionalArgContext):
                            args.append(self.eval_expr(ch.expr()))
                        else:
                            key = text_of(ch.ID())
                            kwargs[key] = self.eval_expr(ch.expr())
                return fn(*args, **kwargs)
            if fname not in self.functions:
                raise ValueError(f"Undefined function: {fname}")
            fdef = self.functions[fname]
            vals = {}
            idx  = 0
            if args_ctx:
                for ch in args_ctx.children:
                    if text_of(ch) == ',': continue
                    if isinstance(ch, CircuitryParser.FunctionCallKeywordArgContext):
                        key = text_of(ch.ID())
                        vals[key] = self.eval_expr(ch.expr())
                    else:
                        param = fdef['params'][idx]
                        vals[param] = self.eval_expr(ch.expr())
                        idx += 1
            for p in fdef['params']:
                if p not in vals:
                    raise ValueError(f"Missing argument: {p}")
            old_vars = self.variables.copy()
            self.variables.update(vals)
            res = self.eval_expr(fdef['body'])
            self.variables = old_vars
            return res

        # boolean literals
        if isinstance(ctx, CircuitryParser.TrueLiteralExprContext):
            return True
        if isinstance(ctx, CircuitryParser.FalseLiteralExprContext):
            return False

        # relational → 1/0
        if isinstance(ctx, CircuitryParser.RelationalExprContext):
            l = self.eval_expr(ctx.expr(0))
            r = self.eval_expr(ctx.expr(1))
            t = ctx.op.type
            return {
                CircuitryParser.LESS:          1 if l < r else 0,
                CircuitryParser.GREATER:       1 if l > r else 0,
                CircuitryParser.LESS_EQUAL:    1 if l <= r else 0,
                CircuitryParser.GREATER_EQUAL: 1 if l >= r else 0,
                CircuitryParser.EQUAL:         1 if l == r else 0,
                CircuitryParser.NOT_EQUAL:     1 if l != r else 0
            }[t]

        # logical in expressions
        if isinstance(ctx, CircuitryParser.NotExprContext):
            return not self.eval_expr(ctx.expr())
        if isinstance(ctx, (CircuitryParser.AndExprContext, CircuitryParser.OrExprContext)):
            l = self.eval_expr(ctx.expr(0))
            r = self.eval_expr(ctx.expr(1))
            return (l and r) if ctx.op.type == CircuitryParser.AND else (l or r)

        # arithmetic
        if hasattr(ctx, 'op') and ctx.op is not None:
            l = self.eval_expr(ctx.expr(0))
            r = self.eval_expr(ctx.expr(1))
            t = ctx.op.type
            return {
                CircuitryParser.PLUS:     l + r,
                CircuitryParser.MINUS:    l - r,
                CircuitryParser.MULTIPLY: l * r,
                CircuitryParser.DIVIDE:   l / r,
                CircuitryParser.EXPONENT: l ** r,
                CircuitryParser.MODULO:   l % r
            }[t]

        # parentheses
        if ctx.getChildCount() == 3 and text_of(ctx.getChild(0)) == '(':
            inner = next(c for c in ctx.children if hasattr(c, 'expr'))
            return self.eval_expr(inner)

        # single token
        if ctx.getChildCount() == 1:
            tok = text_of(ctx)
            if tok in self.variables:
                return self.variables[tok]
            try:
                return parse_value(tok)
            except ValueError:
                raise ValueError(f"Unknown literal or variable: {tok}")

        raise ValueError(f"Cannot evaluate expression: {text_of(ctx)}")
