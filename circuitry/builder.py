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
        self.functions = {}  # function name -> {'params': [...], 'body': ctx.expr()}

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

    def exitFunctionStatement(self, ctx):
        fname = ctx.ID().getText()
        params = [param.getText() for param in ctx.parameterList().ID()]
        expr = ctx.expr()  # Assuming fn returns a single expression
        self.functions[fname] = {'params': params, 'body': expr}

    def eval_expr(self, ctx):
        # Function call
        if isinstance(ctx, CircuitryParser.FuncCallExprContext):
            func_name = ctx.functionCall().ID().getText()
            call_args_ctx = ctx.functionCall().functionCallArgs()

            if func_name not in self.functions:
                raise ValueError(f"Undefined function: {func_name}")

            func_def = self.functions[func_name]
            param_names = func_def['params']
            param_count = len(param_names)

            # Initialize args map
            arg_values = {}

            # If there are any arguments
            if call_args_ctx:
                for arg_ctx in call_args_ctx.functionCallArg():
                    if arg_ctx.ASSIGN():
                        # Keyword argument: name = value
                        key = arg_ctx.ID().getText()
                        val = self.eval_expr(arg_ctx.expr())
                        if key not in param_names:
                            raise ValueError(f"Function {func_name} got unknown keyword argument: {key}")
                        arg_values[key] = val
                    else:
                        # Positional argument
                        idx = len(arg_values)
                        if idx >= param_count:
                            raise ValueError(
                                f"Function {func_name} takes {param_count} arguments, but more were given.")
                        key = param_names[idx]
                        val = self.eval_expr(arg_ctx.expr())
                        arg_values[key] = val

            # Ensure all parameters are filled
            missing = [p for p in param_names if p not in arg_values]
            if missing:
                raise ValueError(f"Missing arguments for function {func_name}: {missing}")

            # Temporarily override variable context
            old_vars = self.variables.copy()
            self.variables.update(arg_values)

            result = self.eval_expr(func_def['body'])
            self.variables = old_vars
            return result

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
