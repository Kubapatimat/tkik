# Generated from Circuitry.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CircuitryParser import CircuitryParser
else:
    from CircuitryParser import CircuitryParser

# This class defines a complete listener for a parse tree produced by CircuitryParser.
class CircuitryListener(ParseTreeListener):

    # Enter a parse tree produced by CircuitryParser#circuit.
    def enterCircuit(self, ctx:CircuitryParser.CircuitContext):
        pass

    # Exit a parse tree produced by CircuitryParser#circuit.
    def exitCircuit(self, ctx:CircuitryParser.CircuitContext):
        pass


    # Enter a parse tree produced by CircuitryParser#statement.
    def enterStatement(self, ctx:CircuitryParser.StatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#statement.
    def exitStatement(self, ctx:CircuitryParser.StatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#component.
    def enterComponent(self, ctx:CircuitryParser.ComponentContext):
        pass

    # Exit a parse tree produced by CircuitryParser#component.
    def exitComponent(self, ctx:CircuitryParser.ComponentContext):
        pass


    # Enter a parse tree produced by CircuitryParser#coord.
    def enterCoord(self, ctx:CircuitryParser.CoordContext):
        pass

    # Exit a parse tree produced by CircuitryParser#coord.
    def exitCoord(self, ctx:CircuitryParser.CoordContext):
        pass



del CircuitryParser