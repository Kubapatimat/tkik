import logging
import math
import sys

from antlr4 import FileStream, CommonTokenStream

from circuitry.builder import CircuitBuilderVisitor
from circuitry.error_listener import FriendlyErrorListener
from circuitry.gen.CircuitryLexer import CircuitryLexer
from circuitry.gen.CircuitryParser import CircuitryParser
from circuitry.utils import to_polar_str

FILE_EXTENSION = '.cty'

def main():
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) != 2:
        print("Usage: python circuitry.py <circuit_file>")
        sys.exit(1)

    if not sys.argv[1].endswith(FILE_EXTENSION):
        print(f"Error: The input file must have a {FILE_EXTENSION} extension.")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r'):
            pass
    except FileNotFoundError:
        print(f"Error: The file '{sys.argv[1]}' does not exist or is not readable.")
        sys.exit(1)

    # 1) Setup ANTLR with our listener
    input_stream = FileStream(sys.argv[1], encoding='utf-8')
    listener = FriendlyErrorListener(input_stream)

    lexer = CircuitryLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(listener)

    stream = CommonTokenStream(lexer)
    parser = CircuitryParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(listener)

    # 2) Parse
    tree = parser.program()

    # 3) Print syntax-error summary and exit immediately if any
    if listener.reportAllErrors():
        sys.exit(1)

    # 4) No syntax errors → run semantic visitor and emit warnings
    visitor = CircuitBuilderVisitor(error_listener=listener)
    visitor.visit(tree)

    # 5) Print summary of semantic warnings (only shown if no syntax errors)
    if listener.warnings:
        print(f"⚠️  Wykryto {len(listener.warnings)} warning(ów).")

    # 6) Run simulations
    simulations = visitor.simulations
    for sim in simulations:
        sim_type = sim.get("type", "dc").lower()
        sim_params = sim.get("params", {})

        if sim_type == "dc":
            from circuitry.mna import dc_solve, element_voltage, element_current
            ground, nodes, vs_list, solution, node_map, n = dc_solve(
                components=visitor.components,
                aliases=visitor.aliases,
                tol=1e-8,
                max_iter=50,
            )
            omega = None

        elif sim_type == "ac":
            from circuitry.mna import ac_solve, element_voltage, element_current
            frequency = sim_params[0]
            ground, nodes, vs_list, solution, node_map, n = ac_solve(
                components=visitor.components,
                aliases=visitor.aliases,
                frequency=frequency,
                tol=1e-8,
                max_iter=50,
            )
            omega = 2 * math.pi * frequency

        else:
            print(f"Error: Unsupported simulation type '{sim_type}'.")
            sys.exit(1)

        print(f"Ground: {ground} = 0 V")
        print("Node voltages:")
        for node, v in zip(nodes, solution[:len(nodes)]):
            if sim_type == "ac":
                print(f"  {node}: {to_polar_str(v)} V")
            else:
                print(f"  {node}: {v:.6f} V")

        print("Voltage source currents:")
        for vs, i in zip(vs_list, solution[len(nodes):]):
            if sim_type == "ac":
                print(f"  {vs.name}: {to_polar_str(i)} A")
            else:
                print(f"  {vs.name}: {i:.6f} A")

        print("Element voltages and currents:")
        for comp in visitor.components:
            v = element_voltage(comp, node_map, ground, solution, visitor.aliases)
            i = element_current(
                comp, node_map, ground, solution, vs_list, n,
                visitor.aliases, omega=omega
            )
            if sim_type == "ac":
                v_str = to_polar_str(v) if isinstance(v, complex) else f"{v:.6f} V"
                i_str = to_polar_str(i) if isinstance(i, complex) else (
                    f"{i:.6f} A" if i is not None else "N/A")
            else:
                v_str = f"{v:.6f} V"
                i_str = f"{i:.6f} A" if i is not None else "N/A"
            print(f"  {comp.name}: Voltage = {v_str}, Current = {i_str}")

if __name__ == "__main__":
    main()
