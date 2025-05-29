from antlr4.error.ErrorListener import ErrorListener


class FriendlyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"Syntax error at line {line}, column {column}: {msg}")
