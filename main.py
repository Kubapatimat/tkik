import sys

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker, InputStream

from circuitry.builder import CircuitBuilder
from circuitry.mna_solver import build_mna
from circuitry.gen.CircuitryLexer import CircuitryLexer
from circuitry.gen.CircuitryParser import CircuitryParser

from circuitry.error_listener import FriendlyErrorListener


def main():
    input_stream = FileStream(sys.argv[1], encoding='utf-8')
    lexer = CircuitryLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CircuitryParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(FriendlyErrorListener())
    tree = parser.program()


    builder = CircuitBuilder()
    walker = ParseTreeWalker()
    walker.walk(builder, tree)

    ground, nodes, volt_sources, sol = build_mna(builder.components, builder.aliases)

    n = len(nodes)

    print(f"Ground node: {ground} (0 V)")
    print("\nNode Voltages:")
    for i, node in enumerate(nodes):
        print(f"  {node}: {sol[i]:.6f} V")

    print("\nVoltage Source Currents:")
    for k, vs in enumerate(volt_sources):
        print(f"  {vs.name}: {sol[n + k]:.6f} A")


if __name__ == "__main__":
    try:
        main()
    except SyntaxError as e:
        print(f"Syntax error: {e}")
    except ValueError as e:
        print(f"Semantic error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


