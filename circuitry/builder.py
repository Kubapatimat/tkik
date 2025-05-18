from circuitry.component import Component
from circuitry.evaluator import parse_value
from circuitry.gen.CircuitryParser import CircuitryParser
from circuitry.gen.CircuitryParserListener import CircuitryParserListener


def get_id_text(mapping, index=0):
    ids = mapping.ID()
    # if ids is a list (multiple IDs), get the one at `index`
    if isinstance(ids, list):
        return ids[index].getText()
    else:
        # single TerminalNodeImpl returned
        if index == 0:
            return ids.getText()
        else:
            raise IndexError("Trying to access index > 0 but only one ID exists.")


class CircuitBuilder(CircuitryParserListener):
    def __init__(self):
        self.components = []
        self.aliases = {}
        self.variables = {}

    def exitAliasStatement(self, ctx):
        for alias in ctx.aliasAssignment():
            alias_name = alias.ID(0).getText()
            original_name = alias.ID(1).getText()
            self.aliases[alias_name] = original_name

    def exitLetStatement(self, ctx):
        for assignCtx in ctx.letAssignment():
            name = assignCtx.ID().getText()
            val = self.eval_expr(assignCtx.expr())
            self.variables[name] = val

    def exitComponentStatement(self, ctx):
        ctype = ctx.componentType().getText()
        name = ctx.ID().getText()
        value = self.eval_expr(ctx.expr())

        nodes = []
        for mapping in ctx.nodeList().nodeMapping():
            kind = type(mapping).__name__

            if kind == "DirectNodeContext":
                nodes.append(get_id_text(mapping, 0))

            elif kind == "RemappedNodeContext":
                nodes.append(get_id_text(mapping, 1))

            elif kind == "SubNodeContext":
                nodes.append(mapping.getText())

            else:
                raise ValueError(f"Unknown nodeMapping type: {kind}")

        self.components.append(Component(ctype, name, value, nodes))

    def eval_expr(self, ctx):
        if ctx is None:
            return 0.0

        # If this node has a binary operator
        if hasattr(ctx, 'op') and ctx.op is not None:
            left = self.eval_expr(ctx.expr(0))
            right = self.eval_expr(ctx.expr(1))
            op = ctx.op.text
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                return left / right
            elif op == '^':
                return left ** right
            elif op == '%':
                return left % right
            else:
                raise ValueError(f"Unsupported operator: {op}")

        # Parentheses (expr in parentheses)
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.eval_expr(ctx.expr(0))

        # Single child node: either a VALUE or ID
        if ctx.getChildCount() == 1:
            child = ctx.getChild(0)
            text = child.getText()

            # Check if it's a variable name (ID)
            # We check if ctx is IdExpr context or text matches a known variable
            # The grammar uses labels, so ctx.IdExpr or ctx.ValueExpr etc. can be checked if needed
            if ctx.getRuleIndex() == CircuitryParser.RULE_expr:
                # Try variable lookup
                if text in self.variables:
                    return self.variables[text]
                # Try parsing value
                try:
                    return parse_value(text)
                except ValueError:
                    pass
                # If neither, it might be an undefined variable
                raise ValueError(
                    f"Undefined variable or invalid value: {text}. Available: {list(self.variables.keys())}")

        raise ValueError(f"Unsupported expression: {ctx.getText()}")
