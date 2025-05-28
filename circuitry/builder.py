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

    def exitFunctionDefinition(self, ctx):
        fname = ctx.ID().getText()
        print("Zdefiniowano funkcję:", fname)
        params = [param.getText() for param in ctx.functionParams().functionParam()] if ctx.functionParams() else []

        # Extract the return expression from the function body
        return_expr = ctx.functionBody().returnStatement().expr()

        self.functions[fname] = {
            'params': params,
            'body': return_expr
        }

    def eval_expr(self, ctx):
        def get_expr(ctx, index=0):
            """Safely get expr(index) or expr() depending on the context type."""
            expr_method = ctx.expr
            try:
                return expr_method(index)
            except TypeError:
                if index == 0:
                    return expr_method()
                raise IndexError("This context only supports expr() with no arguments.")

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
                for child in call_args_ctx.children:
                    # Skip commas
                    if child.getText() == ',':
                        continue

                    if isinstance(child, CircuitryParser.FunctionCallKeywordArgContext):
                        key = child.ID().getText()
                        val = self.eval_expr(child.expr())
                        if key not in param_names:
                            raise ValueError(f"Function {func_name} got unknown keyword argument: {key}")
                        arg_values[key] = val

                    elif isinstance(child, CircuitryParser.FunctionCallPositionalArgContext):
                        idx = len(arg_values)
                        if idx >= param_count:
                            raise ValueError(
                                f"Function {func_name} takes {param_count} arguments, but more were given.")
                        key = param_names[idx]
                        val = self.eval_expr(child.expr())
                        arg_values[key] = val

                    else:
                        raise ValueError(f"Unexpected child in functionCallArgs: {type(child)}")

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
            left = self.eval_expr(get_expr(ctx, 0))
            right = self.eval_expr(get_expr(ctx, 1))
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
            return self.eval_expr(get_expr(ctx, 0))

        # Single child node: either a VALUE or ID
        if ctx.getChildCount() == 1:
            child = ctx.getChild(0)
            text = child.getText()

            # Check if it's a variable name (ID)
            if ctx.getRuleIndex() == CircuitryParser.RULE_expr:
                if text in self.variables:
                    return self.variables[text]
                try:
                    return parse_value(text)
                except ValueError:
                    pass
                raise ValueError(
                    f"Undefined variable or invalid value: {text}. Available: {list(self.variables.keys())}")

        raise ValueError(f"Unsupported expression: {ctx.getText()}")

