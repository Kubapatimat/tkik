// $antlr-format alignTrailingComments true, columnLimit 150, minEmptyLines 1, maxEmptyLinesToKeep 1, reflowComments false, useTab false
// $antlr-format allowShortRulesOnASingleLine false, allowShortBlocksOnASingleLine true, alignSemicolons hanging, alignColons hanging

parser grammar CircuitryParser;

options {
    tokenVocab = CircuitryLexer;
}

program
    : importStatement* circuitStatement* measurementStatement* simulationStatement* drawingStatement* EOF
    ;

// ────────────────────────────────── Import Section ───────────────────────────────────
importStatement
    : IMPORT ID (COMMA ID)* SEMICOLON
    ;

// ───────────────────────────── Circuit Topology Section ──────────────────────────────
circuitStatement
    : aliasStatement
    | letStatement
    | componentStatement
    | seriesStatement
    | parallelStatement
    | assignmentStatement
    | expressionStatement
    | ifStatement
    | whileStatement
    | doWhileStatement
    | forStatement
    | switchStatement
    | functionDefinition
    | subcircuitDefinition
    ;

// Alias statement
aliasStatement
    : ALIAS aliasAssignment (COMMA aliasAssignment)* SEMICOLON
    ;

aliasAssignment
    : ID ASSIGN ID
    ;

// Let statement
letStatement
    : LET letAssignment (COMMA letAssignment)* SEMICOLON
    ;

letAssignment
    : ID ASSIGN expr
    ;

// Component statement
componentStatement
    : componentType ID ASSIGN expr COLON nodeList SEMICOLON
    ;

componentType
    : ID
    ;

nodeList
    : nodeMapping (COMMA nodeMapping)*
    ;

nodeMapping
    : ID                   # DirectNode
    | ID RARROW ID         # RemappedNode
    | ID (DOT dottedNode)+ # SubNode
    ;

dottedNode
    : ID
    | PLUS
    | MINUS
    ;

// Series statement
seriesStatement
    : SERIES ID? COLON nodeList LBRACE seriesBody RBRACE SEMICOLON
    ;

nestedSeriesStatement
    : SERIES ID? LBRACE seriesBody RBRACE
    ;

seriesBody
    : seriesElement (COMMA seriesElement)*
    ;

seriesElement
    : seriesAssignment
    | nestedSeriesStatement
    | nestedParallelStatement
    ;

seriesAssignment
    : componentType ID ASSIGN expr (COLON REVERSED)?
    ;

// Parallel statement
parallelStatement
    : PARALLEL ID? COLON nodeList LBRACE parallelBody RBRACE SEMICOLON
    ;

nestedParallelStatement
    : PARALLEL ID? LBRACE parallelBody RBRACE
    ;

parallelBody
    : parallelElement (COMMA parallelElement)*
    ;

parallelElement
    : parallelAssignment
    | nestedSeriesStatement
    | nestedParallelStatement
    ;

parallelAssignment
    : componentType ID ASSIGN expr (COLON REVERSED)?
    ;

// Assignment statement
assignmentStatement
    : ID unaryAssignmentOperator SEMICOLON
    | ID binaryAssignmentOperator expr SEMICOLON
    ;

unaryAssignmentOperator
    : INC
    | DEC
    ;

binaryAssignmentOperator
    : ASSIGN
    | ADD_ASSIGN
    | SUB_ASSIGN
    | MUL_ASSIGN
    | DIV_ASSIGN
    | MOD_ASSIGN
    | EXP_ASSIGN
    ;

expr
    : <assoc = right> expr EXPONENT expr                                               # ExpExpr
    | expr op = (MULTIPLY | DIVIDE) expr                                               # MulDivExpr
    | expr MODULO expr                                                                 # ModExpr
    | expr op = (PLUS | MINUS) expr                                                    # AddSubExpr
    | expr op = (EQUAL | NOT_EQUAL | LESS | GREATER | LESS_EQUAL | GREATER_EQUAL) expr # RelationalExpr
    | expr op = AND expr                                                               # AndExpr
    | expr op = OR expr                                                                # OrExpr
    | NOT expr                                                                         # NotExpr
    | functionCall                                                                     # FuncCallExpr
    | LPAREN expr RPAREN                                                               # ParenExpr
    | FLOAT_LITERAL                                                                    # FloatLiteralExpr
    | STRING_LITERAL                                                                   # StringLiteralExpr
    | TRUE                                                                             # TrueLiteralExpr
    | FALSE                                                                            # FalseLiteralExpr
    | ID                                                                               # IdExpr
    ;

// Expression statement
expressionStatement
    : expr SEMICOLON
    ;

functionCall
    : ID LPAREN functionCallArgs? RPAREN
    ;

functionCallArgs
    : functionCallArg (COMMA functionCallArg)*
    ;

functionCallArg
    : functionCallKeywordArg
    | functionCallPositionalArg
    ;

functionCallKeywordArg
    : ID ASSIGN expr
    ;

functionCallPositionalArg
    : expr
    ;

// If statement
ifStatement
    : IF LPAREN expr RPAREN block (ELSE block)?
    ;

relationalOperator
    : EQUAL
    | NOT_EQUAL
    | LESS
    | GREATER
    | LESS_EQUAL
    | GREATER_EQUAL
    ;

block
    : LBRACE circuitStatement* RBRACE
    ;

// While statement
whileStatement
    : WHILE LPAREN expr RPAREN block
    ;

// Do while statement
doWhileStatement
    : DO block WHILE LPAREN expr RPAREN SEMICOLON
    ;

// For statement
forStatement
    : FOR LPAREN forInit? SEMICOLON expr? SEMICOLON forUpdate? RPAREN block
    ;

forInit
    : LET letAssignment                # ForInitLet
    | letAssignment                    # ForInitAssign
    | ID unaryAssignmentOperator       # ForInitIncDec
    | ID binaryAssignmentOperator expr # ForInitBinOp
    ;

forUpdate
    : ID unaryAssignmentOperator       # ForUpdateIncDec
    | ID binaryAssignmentOperator expr # ForUpdateBinOp
    ;

// Switch statement
switchStatement
    : SWITCH LPAREN expr RPAREN LBRACE caseStatement* defaultStatement? RBRACE
    ;

caseStatement
    : CASE expr COLON block
    ;

defaultStatement
    : DEFAULT COLON block
    ;

// Function definition
functionDefinition
    : FN ID LPAREN functionParams? RPAREN functionBlock
    ;

functionParams
    : functionParam (COMMA functionParam)*
    ;

functionParam
    : ID (ASSIGN expr)?
    ;

functionBlock
    : LBRACE (circuitStatement | returnStatement)* RBRACE
    ;

returnStatement
    : RETURN expr SEMICOLON
    ;

// Subcircuit definition
subcircuitDefinition
    : SUBCIRCUIT ID LPAREN subcircuitParams? RPAREN COLON nodeList LBRACE circuitStatement* RBRACE
    ;

subcircuitParams
    : subcircuitParam (COMMA subcircuitParam)*
    ;

subcircuitParam
    : ID (ASSIGN expr)?
    ;

// ──────────────────────────── Circuit Simulation Section ─────────────────────────────
simulationStatement
    : simulationType LPAREN functionCallArgs? RPAREN SEMICOLON
    ;

simulationType
    : AC
    | DC
    | TRANSIENT
    ;

// ──────────────────────────── Circuit Measurement Section ────────────────────────────
measurementStatement
    : MEASURE ID
    ;

// ────────────────────────────── Circuit Drawing Section ──────────────────────────────
drawingStatement
    : POS ID ASSIGN LPAREN FLOAT_LITERAL COMMA FLOAT_LITERAL RPAREN SEMICOLON
    ;