from antlr4.error.ErrorListener import ErrorListener

class FriendlyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"Błąd składni w linii {line}, kolumna {column}: {msg}")
