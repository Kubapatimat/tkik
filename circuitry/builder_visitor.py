from antlr4 import ParseTreeVisitor
from circuitry.gen.CircuitryParser import CircuitryParser
from circuitry.component import Component
from circuitry.evaluator import parse_value
import math

class BuilderVisitor(ParseTreeVisitor):
    def __init__(self):
        self.components = []
        self.aliases    = {}
        self.variables  = {"pi": math.pi}
        self.builtins   = {
            "sqrt": math.sqrt,
            "sine": lambda **kwargs: {"type": "sine", **kwargs}
        }
        self.functions  = {}

    # --- program & dispatch ---
    def visitProgram(self, ctx:CircuitryParser.ProgramContext):
        for stmt in ctx.topologyStatement():
            self.visit(stmt)
        return self

    def visitTopologyStatement(self, ctx:CircuitryParser.TopologyStatementContext):
        # jedna z możliwych instrukcji
        if ctx.aliasStatement():      return self.visit(ctx.aliasStatement())
        if ctx.letStatement():        return self.visit(ctx.letStatement())
        if ctx.componentStatement():  return self.visit(ctx.componentStatement())
        if ctx.ifStatement():         return self.visit(ctx.ifStatement())
        if ctx.forStatement():        return self.visit(ctx.forStatement())
        # (inne: series, parallel, assignment, itd. można dodać analogicznie)
        return None

    # --- alias i let ---
    def visitAliasStatement(self, ctx):
        for a in ctx.aliasAssignment():
            name = a.ID().getText()
            val_ctx = a.expr()
            if isinstance(val_ctx, CircuitryParser.IdExprContext):
                val = val_ctx.getText()
            else:
                val = str(self.eval_expr(val_ctx))
            self.aliases[name] = val

    def visitLetStatement(self, ctx):
        for l in ctx.letAssignment():
            name = l.ID().getText()
            val  = self.eval_expr(l.expr())
            self.variables[name] = val

    # --- komponent ---
    def visitComponentStatement(self, ctx):
        ctype = ctx.componentType().getText()
        name  = ctx.ID().getText()
        value = self.eval_expr(ctx.expr())
        nodes = []
        for m in ctx.nodeList().nodeMapping():
            kind = type(m).__name__
            if kind=="DirectNodeContext":
                nodes.append(m.ID(0).getText())
            elif kind=="RemappedNodeContext":
                nodes.append(m.ID(1).getText())
            else:  # SubNode albo inne
                nodes.append(m.getText())
        self.components.append(Component(ctype, name, value, nodes))

    # --- if/else ---
    def visitIfStatement(self, ctx:CircuitryParser.IfStatementContext):
        # pierwsze "if"
        cond = self.eval_bool(ctx.booleanExpr())
        if cond:
            # blok klamrowy albo pojedyncza instrukcja
            if ctx.IfBlock():
                for s in ctx.IfBlock().topologyStatement():
                    self.visit(s)
            else:
                self.visit(ctx.IfSingle().topologyStatement())
            return
        # else, jeśli jest
        if ctx.ELSE():
            if ctx.ElseBlock():
                for s in ctx.ElseBlock().topologyStatement():
                    self.visit(s)
            else:
                self.visit(ctx.ElseSingle().topologyStatement())

    # --- for ---
    def visitForStatement(self, ctx:CircuitryParser.ForStatementContext):
        # init
        if ctx.forInit():
            fi = ctx.forInit()
            # letInit: zawsze forma ID ASSIGN expr
            if fi.letAssignment():
                name = fi.letAssignment().ID().getText()
                val  = self.eval_expr(fi.letAssignment().expr())
                self.variables[name] = val
            # można by obsłużyć assignmentStatement(), ale tu wystarczy let

        # warunek pętli
        cond_ctx = ctx.booleanExpr()
        # update
        upd = ctx.forUpdate()

        # ciało
        body = ctx.topologyStatement()

        # wykonuj dopóki warunek True
        while self.eval_bool(cond_ctx):
            # każdego kroku odwiedź wszystkie instrukcje w ciele
            for s in body:
                self.visit(s)

            # update (np. i = i + 1)
            if upd:
                # assignmentStatement: ID binaryAssign expr SEMI
                bin = upd.assignmentStatement()
                if bin:
                    var = bin.ID().getText()
                    op  = bin.binaryAssignmentOperator().getText()
                    val = self.eval_expr(bin.expr())
                    if op == "=":
                        self.variables[var] = val
                    elif op == "+=":
                        self.variables[var] += val
                    # (można dodać resztę operatorów)
        # koniec for

    # --- wyrażenia logiczne do warunku pętli/if ---
    def eval_bool(self, bctx):
        if bctx.relationalOperator():
            l = self.eval_expr(bctx.expr(0)); r = self.eval_expr(bctx.expr(1))
            op = bctx.relationalOperator().getText()
            return {"<":l<r,">":l>r,"<=":l<=r,">=":l>=r,"==":l==r,"!=":l!=r}[op]
        if bctx.AND():
            return self.eval_expr(bctx.expr(0)) and self.eval_expr(bctx.expr(1))
        if bctx.OR():
            return self.eval_expr(bctx.expr(0)) or self.eval_expr(bctx.expr(1))
        if bctx.NOT():
            return not self.eval_expr(bctx.expr(0))
        # rytualne rzutowanie
        return bool(self.eval_expr(bctx.expr(0)))

    # --- ewaluacja dowolnego expr ---
    def eval_expr(self, ctx):
        # mnożenie/dzielenie, dodawanie...
        if hasattr(ctx, 'op') and ctx.op:
            l = self.eval_expr(ctx.expr(0)); r = self.eval_expr(ctx.expr(1))
            t = ctx.op.text
            if t == '+': return l + r
            if t == '-': return l - r
            if t == '*': return l * r
            if t == '/': return l / r
            if t == '%': return l % r
            if t == '^': return l ** r
            if t == '==': return l == r
            if t == '!=': return l != r
            if t == '<':  return l <  r
            if t == '>':  return l >  r
            if t == '<=': return l <= r
            if t == '>=': return l >= r
        # nawiasy
        from circuitry.gen.CircuitryParser import CircuitryParser
        if isinstance(ctx, CircuitryParser.ParenExprContext):
            return self.eval_expr(ctx.expr())
        # wywołanie funkcji
        if isinstance(ctx, CircuitryParser.FuncCallExprContext):
            fc = ctx.functionCall()
            name = fc.ID().getText()
            args = []
            kwargs = {}
            if fc.functionCallArgs():
                for ch in fc.functionCallArgs().children:
                    txt = ch.getText()
                    if txt == ',': continue
                    if isinstance(ch, CircuitryParser.FunctionCallPositionalArgContext):
                        args.append(self.eval_expr(ch.expr()))
                    else:
                        k = ch.ID().getText(); kwargs[k] = self.eval_expr(ch.expr())
            if name in self.builtins:
                return self.builtins[name](*args, **kwargs)
            # obsługa zdefiniowanych funkcji użytkownika...
        # literały
        if isinstance(ctx, CircuitryParser.TrueLiteralExprContext):  return 1
        if isinstance(ctx, CircuitryParser.FalseLiteralExprContext): return 0
        text = ctx.getText()
        if text in self.variables: return self.variables[text]
        try:
            return parse_value(text)
        except:
            raise ValueError(f"Unknown literal or variable: {text}")

        # nie powinno dojść tutaj
        raise ValueError(f"Cannot eval: {ctx.getText()}")
