# Generated from Circuitry.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CircuitryParser import CircuitryParser
else:
    from CircuitryParser import CircuitryParser

# This class defines a complete generic visitor for a parse tree produced by CircuitryParser.

class CircuitryVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CircuitryParser#circuit.
    def visitCircuit(self, ctx:CircuitryParser.CircuitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#statement.
    def visitStatement(self, ctx:CircuitryParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#component.
    def visitComponent(self, ctx:CircuitryParser.ComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#coord.
    def visitCoord(self, ctx:CircuitryParser.CoordContext):
        return self.visitChildren(ctx)



del CircuitryParser