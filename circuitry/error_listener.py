from antlr4.error.ErrorListener import ErrorListener
from antlr4 import InputStream

class FriendlyErrorListener(ErrorListener):
    def __init__(self, input_stream: InputStream, print_errors: bool = False, suppress_warnings: bool = True):
        super().__init__()
        data = input_stream.getText(0, input_stream.size)
        self.lines = data.splitlines()
        self.had_error = False
        self.warnings = []
        self.errors = []  # zbieramy błędy składniowe i semantyczne
        self.print_errors = print_errors
        self.suppress_warnings = suppress_warnings

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.had_error = True
        error_info = {
            'type': 'syntax',
            'line': line,
            'column': column,
            'msg': msg,
        }
        self.errors.append(error_info)
        if self.print_errors:
            RED    = "\033[31m"
            BOLD   = "\033[1m"
            YELLOW = "\033[33m"
            RESET  = "\033[0m"
            ICON   = "❌"
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
        # Zbieramy warningi, ale nie drukujemy, jeśli suppress_warnings=True
        self.warnings.append((line, column, msg))
        if not self.suppress_warnings:
            YELLOW = "\033[33m"
            BOLD   = "\033[1m"
            RESET  = "\033[0m"
            ICON   = "⚠️"
            header = f"{YELLOW}{BOLD}{ICON} Warning at line {line}, column {column}:{RESET}"
            details = f"{YELLOW}{msg}{RESET}"
            print(header)
            print(f"    {details}\n")

    def semanticError(self, line: int, column: int, msg: str):
        self.had_error = True
        error_info = {
            'type': 'semantic',
            'line': line,
            'column': column,
            'msg': msg,
        }
        self.errors.append(error_info)
        if self.print_errors:
            RED    = "\033[31m"
            BOLD   = "\033[1m"
            RESET  = "\033[0m"
            ICON   = "❌"
            header = f"{RED}{BOLD}{ICON} Semantic error at line {line}, column {column}:{RESET}"
            details = f"{RED}{msg}{RESET}"
            print(header)
            print(f"    {details}\n")

    def reportAllErrors(self) -> bool:
        if self.had_error:
            if self.print_errors:
                print("Kompilacja przerwana z powodu błędów składniowych lub semantycznych.")
            return True
        return False

    def getErrors(self):
        return self.errors