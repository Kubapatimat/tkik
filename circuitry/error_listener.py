import sys
from antlr4.error.ErrorListener import ErrorListener
from antlr4 import InputStream

class FriendlyErrorListener(ErrorListener):
    def __init__(self, input_stream: InputStream):
        super().__init__()
        data = input_stream.getText(0, input_stream.size)
        self.lines = data.splitlines()
        self.had_syntax_error = False
        self.syntax_errors = []   # lista tuple (line, column, msg)
        self.warnings = []        # lista tuple (line, column, msg)
        self.semantic_errors = [] # lista tuple (line, column, msg)
        # Możesz ustawić na True, by przerywać przy pierwszym błędzie
        self.fail_on_error = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Zbieramy błąd, ale nie wypisujemy go tutaj.
        self.had_syntax_error = True
        self.syntax_errors.append((line, column, msg))
        if self.fail_on_error:
            raise RuntimeError(f"Syntax error at line {line}, column {column}: {msg}")

    def warning(self, line: int, column: int, msg: str):
        # Zbieramy warningi
        self.warnings.append((line, column, msg))
        # nie wypisujemy tutaj — decyzję podejmiemy z zewnątrz

    def semanticError(self, line: int, column: int, msg: str):
        # Zbieramy błąd semantyczny
        self.semantic_errors.append((line, column, msg))
        if self.fail_on_error:
            raise RuntimeError(f"Semantic error at line {line}, column {column}: {msg}")

    def reportAllErrors(self) -> bool:
        """
        Zwraca True, jeśli były błędy składniowe.
        Metoda do wywołania po parsowaniu, aby sprawdzić, czy były błędy.
        """
        return self.had_syntax_error

    def format_syntax_errors(self):
        """
        Zwraca listę sformatowanych komunikatów o błędach składni,
        z prefiksem czerwonego X.
        """
        out = []
        RED = "\033[31m"
        BOLD = "\033[1m"
        RESET = "\033[0m"
        ICON = "❌"
        for (line, column, msg) in self.syntax_errors:
            # Pobierz źródłową linię i wskaźnik
            src_line = ""
            if 1 <= line <= len(self.lines):
                src_line = self.lines[line - 1].replace("\t", "    ")
            pointer = ""
            if src_line:
                pointer = " " * column + "^"
            # Budujemy komunikat z ANSI kolorami
            header = f"{RED}{BOLD}{ICON} Syntax error at line {line}, column {column}:{RESET}"
            details = f"{RED}{msg}{RESET}"
            block = [header, f"    {details}"]
            if src_line:
                block.append(f"    {src_line}")
                block.append(f"    {pointer}")
            out.append("\n".join(block))
        return out

    def format_warnings(self):
        """
        Zwraca listę sformatowanych warningów, z prefiksem żółtego ⚠️.
        """
        out = []
        YELLOW = "\033[33m"
        BOLD = "\033[1m"
        RESET = "\033[0m"
        ICON = "⚠️"
        for (line, column, msg) in self.warnings:
            header = f"{YELLOW}{BOLD}{ICON} Warning at line {line}, column {column}:{RESET}"
            details = f"{YELLOW}{msg}{RESET}"
            out.append("\n".join([header, f"    {details}"]))
        return out

    def format_semantic_errors(self):
        """
        Zwraca listę sformatowanych błędów semantycznych, z prefiksem czerwonego X.
        """
        out = []
        RED = "\033[31m"
        BOLD = "\033[1m"
        RESET = "\033[0m"
        ICON = "❌"
        for (line, column, msg) in self.semantic_errors:
            header = f"{RED}{BOLD}{ICON} Semantic error at line {line}, column {column}:{RESET}"
            details = f"{RED}{msg}{RESET}"
            out.append("\n".join([header, f"    {details}"]))
        return out
