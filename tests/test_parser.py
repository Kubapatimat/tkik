import os
from pathlib import Path

import pytest
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from circuitry.gen.CircuitryLexer import CircuitryLexer
from circuitry.gen.CircuitryParser import CircuitryParser


class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        raise Exception(f"Syntax error at line {line}:{column}: {msg}")


def parse_program(text):
    input_stream = InputStream(text)
    lexer = CircuitryLexer(input_stream)

    lexer.removeErrorListeners()
    lexer.addErrorListener(ThrowingErrorListener())

    stream = CommonTokenStream(lexer)

    parser = CircuitryParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener())

    parser.buildParseTrees = True
    tree = parser.program()
    return tree


EXAMPLES_DIR = Path(__file__).parent.parent / "examples"
example_files = list(EXAMPLES_DIR.glob("*.cty"))


@pytest.mark.parametrize("example_file", example_files)
def test_example_file_parses(example_file):
    source = example_file.read_text(encoding="utf-8")
    try:
        parse_program(source)
    except Exception as e:
        pytest.fail(f"Failed to parse {os.path.basename(example_file)}: {e}")
