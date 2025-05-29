# Generated from E:/Studia/AGH/Semestr 4/ISI/TKIK/tkik/grammar/CircuitryParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CircuitryParser import CircuitryParser
else:
    from CircuitryParser import CircuitryParser

# This class defines a complete listener for a parse tree produced by CircuitryParser.
class CircuitryParserListener(ParseTreeListener):

    # Enter a parse tree produced by CircuitryParser#program.
    def enterProgram(self, ctx:CircuitryParser.ProgramContext):
        pass

    # Exit a parse tree produced by CircuitryParser#program.
    def exitProgram(self, ctx:CircuitryParser.ProgramContext):
        pass


    # Enter a parse tree produced by CircuitryParser#importStatement.
    def enterImportStatement(self, ctx:CircuitryParser.ImportStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#importStatement.
    def exitImportStatement(self, ctx:CircuitryParser.ImportStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#circuitStatement.
    def enterCircuitStatement(self, ctx:CircuitryParser.CircuitStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#circuitStatement.
    def exitCircuitStatement(self, ctx:CircuitryParser.CircuitStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#aliasStatement.
    def enterAliasStatement(self, ctx:CircuitryParser.AliasStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#aliasStatement.
    def exitAliasStatement(self, ctx:CircuitryParser.AliasStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#aliasAssignment.
    def enterAliasAssignment(self, ctx:CircuitryParser.AliasAssignmentContext):
        pass

    # Exit a parse tree produced by CircuitryParser#aliasAssignment.
    def exitAliasAssignment(self, ctx:CircuitryParser.AliasAssignmentContext):
        pass


    # Enter a parse tree produced by CircuitryParser#letStatement.
    def enterLetStatement(self, ctx:CircuitryParser.LetStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#letStatement.
    def exitLetStatement(self, ctx:CircuitryParser.LetStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#letAssignment.
    def enterLetAssignment(self, ctx:CircuitryParser.LetAssignmentContext):
        pass

    # Exit a parse tree produced by CircuitryParser#letAssignment.
    def exitLetAssignment(self, ctx:CircuitryParser.LetAssignmentContext):
        pass


    # Enter a parse tree produced by CircuitryParser#componentStatement.
    def enterComponentStatement(self, ctx:CircuitryParser.ComponentStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#componentStatement.
    def exitComponentStatement(self, ctx:CircuitryParser.ComponentStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#componentType.
    def enterComponentType(self, ctx:CircuitryParser.ComponentTypeContext):
        pass

    # Exit a parse tree produced by CircuitryParser#componentType.
    def exitComponentType(self, ctx:CircuitryParser.ComponentTypeContext):
        pass


    # Enter a parse tree produced by CircuitryParser#nodeList.
    def enterNodeList(self, ctx:CircuitryParser.NodeListContext):
        pass

    # Exit a parse tree produced by CircuitryParser#nodeList.
    def exitNodeList(self, ctx:CircuitryParser.NodeListContext):
        pass


    # Enter a parse tree produced by CircuitryParser#DirectNode.
    def enterDirectNode(self, ctx:CircuitryParser.DirectNodeContext):
        pass

    # Exit a parse tree produced by CircuitryParser#DirectNode.
    def exitDirectNode(self, ctx:CircuitryParser.DirectNodeContext):
        pass


    # Enter a parse tree produced by CircuitryParser#RemappedNode.
    def enterRemappedNode(self, ctx:CircuitryParser.RemappedNodeContext):
        pass

    # Exit a parse tree produced by CircuitryParser#RemappedNode.
    def exitRemappedNode(self, ctx:CircuitryParser.RemappedNodeContext):
        pass


    # Enter a parse tree produced by CircuitryParser#SubNode.
    def enterSubNode(self, ctx:CircuitryParser.SubNodeContext):
        pass

    # Exit a parse tree produced by CircuitryParser#SubNode.
    def exitSubNode(self, ctx:CircuitryParser.SubNodeContext):
        pass


    # Enter a parse tree produced by CircuitryParser#dottedNode.
    def enterDottedNode(self, ctx:CircuitryParser.DottedNodeContext):
        pass

    # Exit a parse tree produced by CircuitryParser#dottedNode.
    def exitDottedNode(self, ctx:CircuitryParser.DottedNodeContext):
        pass


    # Enter a parse tree produced by CircuitryParser#seriesStatement.
    def enterSeriesStatement(self, ctx:CircuitryParser.SeriesStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#seriesStatement.
    def exitSeriesStatement(self, ctx:CircuitryParser.SeriesStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#nestedSeriesStatement.
    def enterNestedSeriesStatement(self, ctx:CircuitryParser.NestedSeriesStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#nestedSeriesStatement.
    def exitNestedSeriesStatement(self, ctx:CircuitryParser.NestedSeriesStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#seriesBody.
    def enterSeriesBody(self, ctx:CircuitryParser.SeriesBodyContext):
        pass

    # Exit a parse tree produced by CircuitryParser#seriesBody.
    def exitSeriesBody(self, ctx:CircuitryParser.SeriesBodyContext):
        pass


    # Enter a parse tree produced by CircuitryParser#seriesElement.
    def enterSeriesElement(self, ctx:CircuitryParser.SeriesElementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#seriesElement.
    def exitSeriesElement(self, ctx:CircuitryParser.SeriesElementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#seriesAssignment.
    def enterSeriesAssignment(self, ctx:CircuitryParser.SeriesAssignmentContext):
        pass

    # Exit a parse tree produced by CircuitryParser#seriesAssignment.
    def exitSeriesAssignment(self, ctx:CircuitryParser.SeriesAssignmentContext):
        pass


    # Enter a parse tree produced by CircuitryParser#parallelStatement.
    def enterParallelStatement(self, ctx:CircuitryParser.ParallelStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#parallelStatement.
    def exitParallelStatement(self, ctx:CircuitryParser.ParallelStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#nestedParallelStatement.
    def enterNestedParallelStatement(self, ctx:CircuitryParser.NestedParallelStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#nestedParallelStatement.
    def exitNestedParallelStatement(self, ctx:CircuitryParser.NestedParallelStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#parallelBody.
    def enterParallelBody(self, ctx:CircuitryParser.ParallelBodyContext):
        pass

    # Exit a parse tree produced by CircuitryParser#parallelBody.
    def exitParallelBody(self, ctx:CircuitryParser.ParallelBodyContext):
        pass


    # Enter a parse tree produced by CircuitryParser#parallelElement.
    def enterParallelElement(self, ctx:CircuitryParser.ParallelElementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#parallelElement.
    def exitParallelElement(self, ctx:CircuitryParser.ParallelElementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#parallelAssignment.
    def enterParallelAssignment(self, ctx:CircuitryParser.ParallelAssignmentContext):
        pass

    # Exit a parse tree produced by CircuitryParser#parallelAssignment.
    def exitParallelAssignment(self, ctx:CircuitryParser.ParallelAssignmentContext):
        pass


    # Enter a parse tree produced by CircuitryParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:CircuitryParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:CircuitryParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#unaryAssignmentOperator.
    def enterUnaryAssignmentOperator(self, ctx:CircuitryParser.UnaryAssignmentOperatorContext):
        pass

    # Exit a parse tree produced by CircuitryParser#unaryAssignmentOperator.
    def exitUnaryAssignmentOperator(self, ctx:CircuitryParser.UnaryAssignmentOperatorContext):
        pass


    # Enter a parse tree produced by CircuitryParser#binaryAssignmentOperator.
    def enterBinaryAssignmentOperator(self, ctx:CircuitryParser.BinaryAssignmentOperatorContext):
        pass

    # Exit a parse tree produced by CircuitryParser#binaryAssignmentOperator.
    def exitBinaryAssignmentOperator(self, ctx:CircuitryParser.BinaryAssignmentOperatorContext):
        pass


    # Enter a parse tree produced by CircuitryParser#AndExpr.
    def enterAndExpr(self, ctx:CircuitryParser.AndExprContext):
        pass

    # Exit a parse tree produced by CircuitryParser#AndExpr.
    def exitAndExpr(self, ctx:CircuitryParser.AndExprContext):
        pass


    # Enter a parse tree produced by CircuitryParser#TrueLiteralExpr.
    def enterTrueLiteralExpr(self, ctx:CircuitryParser.TrueLiteralExprContext):
        pass

    # Exit a parse tree produced by CircuitryParser#TrueLiteralExpr.
    def exitTrueLiteralExpr(self, ctx:CircuitryParser.TrueLiteralExprContext):
        pass


    # Enter a parse tree produced by CircuitryParser#IdExpr.
    def enterIdExpr(self, ctx:CircuitryParser.IdExprContext):
        pass

    # Exit a parse tree produced by CircuitryParser#IdExpr.
    def exitIdExpr(self, ctx:CircuitryParser.IdExprContext):
        pass


    # Enter a parse tree produced by CircuitryParser#FalseLiteralExpr.
    def enterFalseLiteralExpr(self, ctx:CircuitryParser.FalseLiteralExprContext):
        pass

    # Exit a parse tree produced by CircuitryParser#FalseLiteralExpr.
    def exitFalseLiteralExpr(self, ctx:CircuitryParser.FalseLiteralExprContext):
        pass


    # Enter a parse tree produced by CircuitryParser#StringLiteralExpr.
    def enterStringLiteralExpr(self, ctx:CircuitryParser.StringLiteralExprContext):
        pass

    # Exit a parse tree produced by CircuitryParser#StringLiteralExpr.
    def exitStringLiteralExpr(self, ctx:CircuitryParser.StringLiteralExprContext):
        pass


    # Enter a parse tree produced by CircuitryParser#RelationalExpr.
    def enterRelationalExpr(self, ctx:CircuitryParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by CircuitryParser#RelationalExpr.
    def exitRelationalExpr(self, ctx:CircuitryParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by CircuitryParser#ExpExpr.
    def enterExpExpr(self, ctx:CircuitryParser.ExpExprContext):
        pass

    # Exit a parse tree produced by CircuitryParser#ExpExpr.
    def exitExpExpr(self, ctx:CircuitryParser.ExpExprContext):
        pass


    # Enter a parse tree produced by CircuitryParser#OrExpr.
    def enterOrExpr(self, ctx:CircuitryParser.OrExprContext):
        pass

    # Exit a parse tree produced by CircuitryParser#OrExpr.
    def exitOrExpr(self, ctx:CircuitryParser.OrExprContext):
        pass


    # Enter a parse tree produced by CircuitryParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:CircuitryParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by CircuitryParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:CircuitryParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by CircuitryParser#FloatLiteralExpr.
    def enterFloatLiteralExpr(self, ctx:CircuitryParser.FloatLiteralExprContext):
        pass

    # Exit a parse tree produced by CircuitryParser#FloatLiteralExpr.
    def exitFloatLiteralExpr(self, ctx:CircuitryParser.FloatLiteralExprContext):
        pass


    # Enter a parse tree produced by CircuitryParser#NotExpr.
    def enterNotExpr(self, ctx:CircuitryParser.NotExprContext):
        pass

    # Exit a parse tree produced by CircuitryParser#NotExpr.
    def exitNotExpr(self, ctx:CircuitryParser.NotExprContext):
        pass


    # Enter a parse tree produced by CircuitryParser#ModExpr.
    def enterModExpr(self, ctx:CircuitryParser.ModExprContext):
        pass

    # Exit a parse tree produced by CircuitryParser#ModExpr.
    def exitModExpr(self, ctx:CircuitryParser.ModExprContext):
        pass


    # Enter a parse tree produced by CircuitryParser#ParenExpr.
    def enterParenExpr(self, ctx:CircuitryParser.ParenExprContext):
        pass

    # Exit a parse tree produced by CircuitryParser#ParenExpr.
    def exitParenExpr(self, ctx:CircuitryParser.ParenExprContext):
        pass


    # Enter a parse tree produced by CircuitryParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:CircuitryParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by CircuitryParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:CircuitryParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by CircuitryParser#FuncCallExpr.
    def enterFuncCallExpr(self, ctx:CircuitryParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by CircuitryParser#FuncCallExpr.
    def exitFuncCallExpr(self, ctx:CircuitryParser.FuncCallExprContext):
        pass


    # Enter a parse tree produced by CircuitryParser#expressionStatement.
    def enterExpressionStatement(self, ctx:CircuitryParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#expressionStatement.
    def exitExpressionStatement(self, ctx:CircuitryParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#functionCall.
    def enterFunctionCall(self, ctx:CircuitryParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by CircuitryParser#functionCall.
    def exitFunctionCall(self, ctx:CircuitryParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by CircuitryParser#functionCallArgs.
    def enterFunctionCallArgs(self, ctx:CircuitryParser.FunctionCallArgsContext):
        pass

    # Exit a parse tree produced by CircuitryParser#functionCallArgs.
    def exitFunctionCallArgs(self, ctx:CircuitryParser.FunctionCallArgsContext):
        pass


    # Enter a parse tree produced by CircuitryParser#functionCallArg.
    def enterFunctionCallArg(self, ctx:CircuitryParser.FunctionCallArgContext):
        pass

    # Exit a parse tree produced by CircuitryParser#functionCallArg.
    def exitFunctionCallArg(self, ctx:CircuitryParser.FunctionCallArgContext):
        pass


    # Enter a parse tree produced by CircuitryParser#functionCallKeywordArg.
    def enterFunctionCallKeywordArg(self, ctx:CircuitryParser.FunctionCallKeywordArgContext):
        pass

    # Exit a parse tree produced by CircuitryParser#functionCallKeywordArg.
    def exitFunctionCallKeywordArg(self, ctx:CircuitryParser.FunctionCallKeywordArgContext):
        pass


    # Enter a parse tree produced by CircuitryParser#functionCallPositionalArg.
    def enterFunctionCallPositionalArg(self, ctx:CircuitryParser.FunctionCallPositionalArgContext):
        pass

    # Exit a parse tree produced by CircuitryParser#functionCallPositionalArg.
    def exitFunctionCallPositionalArg(self, ctx:CircuitryParser.FunctionCallPositionalArgContext):
        pass


    # Enter a parse tree produced by CircuitryParser#ifStatement.
    def enterIfStatement(self, ctx:CircuitryParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#ifStatement.
    def exitIfStatement(self, ctx:CircuitryParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#relationalOperator.
    def enterRelationalOperator(self, ctx:CircuitryParser.RelationalOperatorContext):
        pass

    # Exit a parse tree produced by CircuitryParser#relationalOperator.
    def exitRelationalOperator(self, ctx:CircuitryParser.RelationalOperatorContext):
        pass


    # Enter a parse tree produced by CircuitryParser#block.
    def enterBlock(self, ctx:CircuitryParser.BlockContext):
        pass

    # Exit a parse tree produced by CircuitryParser#block.
    def exitBlock(self, ctx:CircuitryParser.BlockContext):
        pass


    # Enter a parse tree produced by CircuitryParser#whileStatement.
    def enterWhileStatement(self, ctx:CircuitryParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#whileStatement.
    def exitWhileStatement(self, ctx:CircuitryParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:CircuitryParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:CircuitryParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#forStatement.
    def enterForStatement(self, ctx:CircuitryParser.ForStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#forStatement.
    def exitForStatement(self, ctx:CircuitryParser.ForStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#ForInitLet.
    def enterForInitLet(self, ctx:CircuitryParser.ForInitLetContext):
        pass

    # Exit a parse tree produced by CircuitryParser#ForInitLet.
    def exitForInitLet(self, ctx:CircuitryParser.ForInitLetContext):
        pass


    # Enter a parse tree produced by CircuitryParser#ForInitAssign.
    def enterForInitAssign(self, ctx:CircuitryParser.ForInitAssignContext):
        pass

    # Exit a parse tree produced by CircuitryParser#ForInitAssign.
    def exitForInitAssign(self, ctx:CircuitryParser.ForInitAssignContext):
        pass


    # Enter a parse tree produced by CircuitryParser#ForInitIncDec.
    def enterForInitIncDec(self, ctx:CircuitryParser.ForInitIncDecContext):
        pass

    # Exit a parse tree produced by CircuitryParser#ForInitIncDec.
    def exitForInitIncDec(self, ctx:CircuitryParser.ForInitIncDecContext):
        pass


    # Enter a parse tree produced by CircuitryParser#ForInitBinOp.
    def enterForInitBinOp(self, ctx:CircuitryParser.ForInitBinOpContext):
        pass

    # Exit a parse tree produced by CircuitryParser#ForInitBinOp.
    def exitForInitBinOp(self, ctx:CircuitryParser.ForInitBinOpContext):
        pass


    # Enter a parse tree produced by CircuitryParser#ForUpdateIncDec.
    def enterForUpdateIncDec(self, ctx:CircuitryParser.ForUpdateIncDecContext):
        pass

    # Exit a parse tree produced by CircuitryParser#ForUpdateIncDec.
    def exitForUpdateIncDec(self, ctx:CircuitryParser.ForUpdateIncDecContext):
        pass


    # Enter a parse tree produced by CircuitryParser#ForUpdateBinOp.
    def enterForUpdateBinOp(self, ctx:CircuitryParser.ForUpdateBinOpContext):
        pass

    # Exit a parse tree produced by CircuitryParser#ForUpdateBinOp.
    def exitForUpdateBinOp(self, ctx:CircuitryParser.ForUpdateBinOpContext):
        pass


    # Enter a parse tree produced by CircuitryParser#switchStatement.
    def enterSwitchStatement(self, ctx:CircuitryParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#switchStatement.
    def exitSwitchStatement(self, ctx:CircuitryParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#caseStatement.
    def enterCaseStatement(self, ctx:CircuitryParser.CaseStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#caseStatement.
    def exitCaseStatement(self, ctx:CircuitryParser.CaseStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#defaultStatement.
    def enterDefaultStatement(self, ctx:CircuitryParser.DefaultStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#defaultStatement.
    def exitDefaultStatement(self, ctx:CircuitryParser.DefaultStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:CircuitryParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CircuitryParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:CircuitryParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by CircuitryParser#functionParams.
    def enterFunctionParams(self, ctx:CircuitryParser.FunctionParamsContext):
        pass

    # Exit a parse tree produced by CircuitryParser#functionParams.
    def exitFunctionParams(self, ctx:CircuitryParser.FunctionParamsContext):
        pass


    # Enter a parse tree produced by CircuitryParser#functionParam.
    def enterFunctionParam(self, ctx:CircuitryParser.FunctionParamContext):
        pass

    # Exit a parse tree produced by CircuitryParser#functionParam.
    def exitFunctionParam(self, ctx:CircuitryParser.FunctionParamContext):
        pass


    # Enter a parse tree produced by CircuitryParser#functionBlock.
    def enterFunctionBlock(self, ctx:CircuitryParser.FunctionBlockContext):
        pass

    # Exit a parse tree produced by CircuitryParser#functionBlock.
    def exitFunctionBlock(self, ctx:CircuitryParser.FunctionBlockContext):
        pass


    # Enter a parse tree produced by CircuitryParser#returnStatement.
    def enterReturnStatement(self, ctx:CircuitryParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#returnStatement.
    def exitReturnStatement(self, ctx:CircuitryParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#subcircuitDefinition.
    def enterSubcircuitDefinition(self, ctx:CircuitryParser.SubcircuitDefinitionContext):
        pass

    # Exit a parse tree produced by CircuitryParser#subcircuitDefinition.
    def exitSubcircuitDefinition(self, ctx:CircuitryParser.SubcircuitDefinitionContext):
        pass


    # Enter a parse tree produced by CircuitryParser#subcircuitParams.
    def enterSubcircuitParams(self, ctx:CircuitryParser.SubcircuitParamsContext):
        pass

    # Exit a parse tree produced by CircuitryParser#subcircuitParams.
    def exitSubcircuitParams(self, ctx:CircuitryParser.SubcircuitParamsContext):
        pass


    # Enter a parse tree produced by CircuitryParser#subcircuitParam.
    def enterSubcircuitParam(self, ctx:CircuitryParser.SubcircuitParamContext):
        pass

    # Exit a parse tree produced by CircuitryParser#subcircuitParam.
    def exitSubcircuitParam(self, ctx:CircuitryParser.SubcircuitParamContext):
        pass


    # Enter a parse tree produced by CircuitryParser#simulationStatement.
    def enterSimulationStatement(self, ctx:CircuitryParser.SimulationStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#simulationStatement.
    def exitSimulationStatement(self, ctx:CircuitryParser.SimulationStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#simulationType.
    def enterSimulationType(self, ctx:CircuitryParser.SimulationTypeContext):
        pass

    # Exit a parse tree produced by CircuitryParser#simulationType.
    def exitSimulationType(self, ctx:CircuitryParser.SimulationTypeContext):
        pass


    # Enter a parse tree produced by CircuitryParser#measurementStatement.
    def enterMeasurementStatement(self, ctx:CircuitryParser.MeasurementStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#measurementStatement.
    def exitMeasurementStatement(self, ctx:CircuitryParser.MeasurementStatementContext):
        pass


    # Enter a parse tree produced by CircuitryParser#drawingStatement.
    def enterDrawingStatement(self, ctx:CircuitryParser.DrawingStatementContext):
        pass

    # Exit a parse tree produced by CircuitryParser#drawingStatement.
    def exitDrawingStatement(self, ctx:CircuitryParser.DrawingStatementContext):
        pass



del CircuitryParser