from circuitry.component import Component
from circuitry.evaluator import parse_value
from circuitry.gen.CircuitryParser import CircuitryParser
from circuitry.gen.CircuitryParserListener import CircuitryParserListener
import math


def get_id_text(mapping, index=0):
    ids = mapping.ID()
    if isinstance(ids, list):
        return ids[index].getText()
    else:
        if index == 0:
            return ids.getText()
        else:
            raise IndexError("Trying to access index > 0 but only one ID exists.")


class CircuitBuilder(CircuitryParserListener):
    def __init__(self):
        self.components = []
        self.aliases = {}
        self.variables = {
            "pi": math.pi,
        }
        self.builtins = {
            "sqrt": math.sqrt,
            "sine": lambda **kwargs: {"type": "sine", **kwargs}
        }
        self.functions = {}

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
        return_expr = ctx.functionBody().returnStatement().expr()
        self.functions[fname] = {
            'params': params,
            'body': return_expr
        }

    def eval_expr(self, ctx):
        if isinstance(ctx, CircuitryParser.FuncCallExprContext):
            func_call_ctx = ctx.functionCall()
            func_name = func_call_ctx.ID().getText()
            call_args_ctx = func_call_ctx.functionCallArgs()

            if func_name in self.builtins:
                builtin_func = self.builtins[func_name]

                # Spróbuj najpierw pozycyjnie
                args = []
                kwargs = {}

                if call_args_ctx:
                    for child in call_args_ctx.children:
                        if child.getText() == ',':
                            continue
                        if isinstance(child, CircuitryParser.FunctionCallPositionalArgContext):
                            val = self.eval_expr(child.expr())
                            args.append(val)
                        elif isinstance(child, CircuitryParser.FunctionCallKeywordArgContext):
                            key = child.ID().getText()
                            val = self.eval_expr(child.expr())
                            kwargs[key] = val
                        else:
                            raise ValueError(
                                f"Unexpected argument in call to built-in '{func_name}': {child.getText()}")

                try:
                    return builtin_func(*args, **kwargs)
                except TypeError as e:
                    raise ValueError(f"Error calling built-in '{func_name}': {e}")

            if func_name not in self.functions:
                raise ValueError(f"Undefined function: {func_name}")

            func_def = self.functions[func_name]
            param_names = func_def['params']
            param_count = len(param_names)
            arg_values = {}

            if call_args_ctx:
                for child in call_args_ctx.children:
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
                            raise ValueError(f"Function {func_name} takes {param_count} arguments, but more were given.")
                        key = param_names[idx]
                        val = self.eval_expr(child.expr())
                        arg_values[key] = val
                    else:
                        raise ValueError(f"Unexpected argument in functionCallArgs for {func_name}")

            missing = [p for p in param_names if p not in arg_values]
            if missing:
                raise ValueError(f"Missing arguments for function {func_name}: {missing}")

            old_vars = self.variables.copy()
            self.variables.update(arg_values)
            result = self.eval_expr(func_def['body'])
            self.variables = old_vars
            return result

        if ctx is None:
            return 0.0

        if hasattr(ctx, 'op') and ctx.op is not None:
            subexprs = [c for c in ctx.children if isinstance(c, CircuitryParser.ExprContext)]
            if len(subexprs) != 2:
                raise ValueError("Expected binary operation with two operands.")
            left = self.eval_expr(subexprs[0])
            right = self.eval_expr(subexprs[1])
            op = ctx.op.text
            if op == '+': return left + right
            elif op == '-': return left - right
            elif op == '*': return left * right
            elif op == '/': return left / right
            elif op == '^': return left ** right
            elif op == '%': return left % right
            else: raise ValueError(f"Unsupported operator: {op}")

        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
            subexprs = [c for c in ctx.children if isinstance(c, CircuitryParser.ExprContext)]
            if not subexprs:
                raise ValueError("Empty parentheses in expression.")
            return self.eval_expr(subexprs[0])

        if ctx.getChildCount() == 1:
            child = ctx.getChild(0)
            text = child.getText()
            if ctx.getRuleIndex() == CircuitryParser.RULE_expr:
                if text in self.variables:
                    return self.variables[text]
                try:
                    return parse_value(text)
                except ValueError:
                    raise ValueError(f"Undefined variable or invalid value: {text}")

        raise ValueError(f"Unsupported expression: {ctx.getText()}")
