from antlr4 import *
from CircuitryLexer import CircuitryLexer
from CircuitryParser import CircuitryParser
from CircuitryVisitor import CircuitryVisitor


class CircuitToLatexVisitor(CircuitryVisitor):
    def __init__(self):
        self.lines = []

    def visitCircuit(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
        return self.wrap_latex(self.lines)

    def visitStatement(self, ctx):
        component = ctx.component().getText()
        from_coord = self.parse_coord(ctx.coord(0))
        to_coord = self.parse_coord(ctx.coord(1))
        symbol = {'resistor': 'R', 'capacitor': 'C', 'inductor': 'L'}.get(component, '?')
        self.lines.append(f"\\draw {from_coord} to[{symbol}] {to_coord};")

    def parse_coord(self, coord_ctx):
        x = coord_ctx.INT(0).getText()
        y = coord_ctx.INT(1).getText()
        return f"({x},{y})"

    def wrap_latex(self, draw_lines):
        return (
            "\\begin{circuitikz}\n"
            + "\n".join(draw_lines) +
            "\n\\end{circuitikz}"
        )


def main():
    input_stream = FileStream("example1.circ")
    lexer = CircuitryLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CircuitryParser(stream)
    tree = parser.circuit()

    visitor = CircuitToLatexVisitor()
    output = visitor.visit(tree)

    with open("output.tex", "w") as f:
        f.write(output)

    print("✅ Wygenerowano output.tex")


if __name__ == "__main__":
    main()
