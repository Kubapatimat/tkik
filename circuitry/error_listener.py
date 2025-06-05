# circuitry/error_listener.py

import sys
from antlr4.error.ErrorListener import ErrorListener
from antlr4 import InputStream

class FriendlyErrorListener(ErrorListener):
    def __init__(self, input_stream: InputStream):
        super().__init__()
        data = input_stream.getText(0, input_stream.size)
        self.lines = data.splitlines()
        self.had_error = False

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


    def reportAllErrorsAndExitIfNeeded(self):
        if self.had_error:
            # Można dodatkowo wypisać podsumowanie, np.:
            print("Kompilacja przerwana z powodu błędów składniowych.")
            sys.exit(1)
