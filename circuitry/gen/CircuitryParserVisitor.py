# Generated from E:/Studia/AGH/Semestr 4/ISI/TKIK/tkik/grammar/CircuitryParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CircuitryParser import CircuitryParser
else:
    from CircuitryParser import CircuitryParser

# This class defines a complete generic visitor for a parse tree produced by CircuitryParser.

class CircuitryParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CircuitryParser#program.
    def visitProgram(self, ctx:CircuitryParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#importStatement.
    def visitImportStatement(self, ctx:CircuitryParser.ImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#topologyStatement.
    def visitTopologyStatement(self, ctx:CircuitryParser.TopologyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#aliasStatement.
    def visitAliasStatement(self, ctx:CircuitryParser.AliasStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#aliasAssignment.
    def visitAliasAssignment(self, ctx:CircuitryParser.AliasAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#letStatement.
    def visitLetStatement(self, ctx:CircuitryParser.LetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#letAssignment.
    def visitLetAssignment(self, ctx:CircuitryParser.LetAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#componentStatement.
    def visitComponentStatement(self, ctx:CircuitryParser.ComponentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#componentType.
    def visitComponentType(self, ctx:CircuitryParser.ComponentTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#nodeList.
    def visitNodeList(self, ctx:CircuitryParser.NodeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#DirectNode.
    def visitDirectNode(self, ctx:CircuitryParser.DirectNodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#RemappedNode.
    def visitRemappedNode(self, ctx:CircuitryParser.RemappedNodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#SubNode.
    def visitSubNode(self, ctx:CircuitryParser.SubNodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#dottedNode.
    def visitDottedNode(self, ctx:CircuitryParser.DottedNodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#seriesStatement.
    def visitSeriesStatement(self, ctx:CircuitryParser.SeriesStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#nestedSeriesStatement.
    def visitNestedSeriesStatement(self, ctx:CircuitryParser.NestedSeriesStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#seriesBody.
    def visitSeriesBody(self, ctx:CircuitryParser.SeriesBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#seriesElement.
    def visitSeriesElement(self, ctx:CircuitryParser.SeriesElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#seriesAssignment.
    def visitSeriesAssignment(self, ctx:CircuitryParser.SeriesAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#parallelStatement.
    def visitParallelStatement(self, ctx:CircuitryParser.ParallelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#nestedParallelStatement.
    def visitNestedParallelStatement(self, ctx:CircuitryParser.NestedParallelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#parallelBody.
    def visitParallelBody(self, ctx:CircuitryParser.ParallelBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#parallelElement.
    def visitParallelElement(self, ctx:CircuitryParser.ParallelElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#parallelAssignment.
    def visitParallelAssignment(self, ctx:CircuitryParser.ParallelAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:CircuitryParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#unaryAssignmentOperator.
    def visitUnaryAssignmentOperator(self, ctx:CircuitryParser.UnaryAssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#binaryAssignmentOperator.
    def visitBinaryAssignmentOperator(self, ctx:CircuitryParser.BinaryAssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:CircuitryParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#IdExpr.
    def visitIdExpr(self, ctx:CircuitryParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#FloatLiteralExpr.
    def visitFloatLiteralExpr(self, ctx:CircuitryParser.FloatLiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#StringLiteralExpr.
    def visitStringLiteralExpr(self, ctx:CircuitryParser.StringLiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#ModExpr.
    def visitModExpr(self, ctx:CircuitryParser.ModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#ParenExpr.
    def visitParenExpr(self, ctx:CircuitryParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#ExpExpr.
    def visitExpExpr(self, ctx:CircuitryParser.ExpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:CircuitryParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#FuncCallExpr.
    def visitFuncCallExpr(self, ctx:CircuitryParser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#functionCall.
    def visitFunctionCall(self, ctx:CircuitryParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#functionCallArgs.
    def visitFunctionCallArgs(self, ctx:CircuitryParser.FunctionCallArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#functionCallKeywordArg.
    def visitFunctionCallKeywordArg(self, ctx:CircuitryParser.FunctionCallKeywordArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#functionCallPositionalArg.
    def visitFunctionCallPositionalArg(self, ctx:CircuitryParser.FunctionCallPositionalArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#ifStatement.
    def visitIfStatement(self, ctx:CircuitryParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#conditionWithBlock.
    def visitConditionWithBlock(self, ctx:CircuitryParser.ConditionWithBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#booleanExpr.
    def visitBooleanExpr(self, ctx:CircuitryParser.BooleanExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#relationalOperator.
    def visitRelationalOperator(self, ctx:CircuitryParser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#whileStatement.
    def visitWhileStatement(self, ctx:CircuitryParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:CircuitryParser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#forStatement.
    def visitForStatement(self, ctx:CircuitryParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#forInit.
    def visitForInit(self, ctx:CircuitryParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#forUpdate.
    def visitForUpdate(self, ctx:CircuitryParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#switchStatement.
    def visitSwitchStatement(self, ctx:CircuitryParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#caseStatement.
    def visitCaseStatement(self, ctx:CircuitryParser.CaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#defaultStatement.
    def visitDefaultStatement(self, ctx:CircuitryParser.DefaultStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:CircuitryParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#functionParams.
    def visitFunctionParams(self, ctx:CircuitryParser.FunctionParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#functionParam.
    def visitFunctionParam(self, ctx:CircuitryParser.FunctionParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#functionBody.
    def visitFunctionBody(self, ctx:CircuitryParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#returnStatement.
    def visitReturnStatement(self, ctx:CircuitryParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#subcircuitDefinition.
    def visitSubcircuitDefinition(self, ctx:CircuitryParser.SubcircuitDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#subcircuitParams.
    def visitSubcircuitParams(self, ctx:CircuitryParser.SubcircuitParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#subcircuitParam.
    def visitSubcircuitParam(self, ctx:CircuitryParser.SubcircuitParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#simulationStatement.
    def visitSimulationStatement(self, ctx:CircuitryParser.SimulationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#simulationType.
    def visitSimulationType(self, ctx:CircuitryParser.SimulationTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#measurementStatement.
    def visitMeasurementStatement(self, ctx:CircuitryParser.MeasurementStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitryParser#drawingStatement.
    def visitDrawingStatement(self, ctx:CircuitryParser.DrawingStatementContext):
        return self.visitChildren(ctx)



del CircuitryParser