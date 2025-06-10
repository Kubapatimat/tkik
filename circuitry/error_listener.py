import sys
from antlr4.error.ErrorListener import ErrorListener
from antlr4 import InputStream

class FriendlyErrorListener(ErrorListener):
    def __init__(self, input_stream: InputStream):
        super().__init__()
        data = input_stream.getText(0, input_stream.size)
        self.lines = data.splitlines()
        self.had_error = False
        self.warnings = []


    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        RED    = "\033[31m"
        BOLD   = "\033[1m"
        YELLOW = "\033[33m"
        RESET  = "\033[0m"
        ICON   = "❌"

        self.had_error = True

        header = f"{RED}{BOLD}{ICON} Syntax error at line {line}, column {column}:{RESET}"
        details = f"{RED}{msg}{RESET}"

        src_line = ""
        if 1 <= line <= len(self.lines):
            src_line = self.lines[line - 1].replace("\t", "    ")

        pointer = ""
        if src_line:
            pointer = " " * (column + 4) + f"{YELLOW}^{RESET}"

        print(header)
        print(f"    {details}")
        if src_line:
            print(f"    {src_line}")
            print(pointer)
        print()


    def warning(self, line: int, column: int, msg: str):
        YELLOW = "\033[33m"
        BOLD   = "\033[1m"
        RESET  = "\033[0m"
        ICON   = "⚠️"

        self.warnings.append((line, column, msg))

        header = f"{YELLOW}{BOLD}{ICON} Warning at line {line}, column {column}:{RESET}"
        details = f"{YELLOW}{msg}{RESET}"
        print(header)
        print(f"    {details}")
        print()


    def semanticError(self, line: int, column: int, msg: str):
        RED    = "\033[31m"
        BOLD   = "\033[1m"
        RESET  = "\033[0m"
        ICON   = "❌"

        self.had_error = True

        header = f"{RED}{BOLD}{ICON} Semantic error at line {line}, column {column}:{RESET}"
        details = f"{RED}{msg}{RESET}"
        print(header)
        print(f"    {details}")
        print()


    def reportAllErrors(self) -> bool:
        """
        Print a brief summary of syntax errors.
        Return True if there were any syntax errors.
        """
        if self.had_error:
            print("Kompilacja przerwana z powodu błędów składniowych.")
            return True
        return False
