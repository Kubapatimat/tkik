# Generated from Circuitry.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,34,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,4,0,12,8,0,
        11,0,12,0,13,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,0,0,4,0,2,4,6,0,1,1,0,7,9,30,0,8,1,0,0,0,
        2,18,1,0,0,0,4,25,1,0,0,0,6,27,1,0,0,0,8,9,5,1,0,0,9,11,5,2,0,0,
        10,12,3,2,1,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,
        0,0,0,14,15,1,0,0,0,15,16,5,3,0,0,16,17,5,0,0,1,17,1,1,0,0,0,18,
        19,3,4,2,0,19,20,5,4,0,0,20,21,3,6,3,0,21,22,5,5,0,0,22,23,3,6,3,
        0,23,24,5,6,0,0,24,3,1,0,0,0,25,26,7,0,0,0,26,5,1,0,0,0,27,28,5,
        10,0,0,28,29,5,13,0,0,29,30,5,11,0,0,30,31,5,13,0,0,31,32,5,12,0,
        0,32,7,1,0,0,0,1,13
    ]

class CircuitryParser ( Parser ):

    grammarFileName = "Circuitry.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'draw'", "'{'", "'}'", "'from'", "'to'", 
                     "';'", "'resistor'", "'capacitor'", "'inductor'", "'('", 
                     "','", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "WS" ]

    RULE_circuit = 0
    RULE_statement = 1
    RULE_component = 2
    RULE_coord = 3

    ruleNames =  [ "circuit", "statement", "component", "coord" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    INT=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CircuitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CircuitryParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.StatementContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.StatementContext,i)


        def getRuleIndex(self):
            return CircuitryParser.RULE_circuit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCircuit" ):
                listener.enterCircuit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCircuit" ):
                listener.exitCircuit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCircuit" ):
                return visitor.visitCircuit(self)
            else:
                return visitor.visitChildren(self)




    def circuit(self):

        localctx = CircuitryParser.CircuitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_circuit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(CircuitryParser.T__0)
            self.state = 9
            self.match(CircuitryParser.T__1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.statement()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
                    break

            self.state = 15
            self.match(CircuitryParser.T__2)
            self.state = 16
            self.match(CircuitryParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def component(self):
            return self.getTypedRuleContext(CircuitryParser.ComponentContext,0)


        def coord(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.CoordContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.CoordContext,i)


        def getRuleIndex(self):
            return CircuitryParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CircuitryParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.component()
            self.state = 19
            self.match(CircuitryParser.T__3)
            self.state = 20
            self.coord()
            self.state = 21
            self.match(CircuitryParser.T__4)
            self.state = 22
            self.coord()
            self.state = 23
            self.match(CircuitryParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CircuitryParser.RULE_component

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponent" ):
                listener.enterComponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponent" ):
                listener.exitComponent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComponent" ):
                return visitor.visitComponent(self)
            else:
                return visitor.visitChildren(self)




    def component(self):

        localctx = CircuitryParser.ComponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_component)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitryParser.INT)
            else:
                return self.getToken(CircuitryParser.INT, i)

        def getRuleIndex(self):
            return CircuitryParser.RULE_coord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoord" ):
                listener.enterCoord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoord" ):
                listener.exitCoord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoord" ):
                return visitor.visitCoord(self)
            else:
                return visitor.visitChildren(self)




    def coord(self):

        localctx = CircuitryParser.CoordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_coord)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(CircuitryParser.T__9)
            self.state = 28
            self.match(CircuitryParser.INT)
            self.state = 29
            self.match(CircuitryParser.T__10)
            self.state = 30
            self.match(CircuitryParser.INT)
            self.state = 31
            self.match(CircuitryParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





