// $antlr-format alignTrailingComments true, columnLimit 150, minEmptyLines 1, maxEmptyLinesToKeep 1, reflowComments false, useTab false
// $antlr-format allowShortRulesOnASingleLine false, allowShortBlocksOnASingleLine true, alignSemicolons hanging, alignColons hanging

parser grammar CircuitryParser;

options {
    tokenVocab = CircuitryLexer;
}

program
    : importStatement* topologyStatement* measurementStatement* simulationStatement* drawingStatement* EOF
    ;

// ────────────────────────────────── Import Section ───────────────────────────────────
importStatement
    : IMPORT ID (COMMA ID)* SEMICOLON
    ;

// ───────────────────────────── Circuit Topology Section ──────────────────────────────
topologyStatement
    : aliasStatement
    | letStatement
    | componentStatement
    | seriesStatement
    | parallelStatement
    | assignmentStatement
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
    : <assoc = right> expr EXPONENT expr # ExpExpr
    | expr op = (MULTIPLY | DIVIDE) expr # MulDivExpr
    | expr MODULO expr                   # ModExpr
    | expr op = (PLUS | MINUS) expr      # AddSubExpr
    | functionCall                       # FuncCallExpr
    | LPAREN expr RPAREN                 # ParenExpr
    | FLOAT_LITERAL                      # FloatLiteralExpr
    | STRING_LITERAL                     # StringLiteralExpr
    | ID                                 # IdExpr
    ;

functionCall
    : ID LPAREN functionCallArgs? RPAREN
    ;

functionCallArgs
    : functionCallArg (COMMA functionCallArg)*
    ;

functionCallArg
    : ID ASSIGN expr // keyword argument
    | expr           // positional argument
    ;

// If statement
ifStatement
    : IF conditionWithBlock (ELSE IF conditionWithBlock)* (ELSE topologyStatement*)?
    ;

conditionWithBlock
    : LPAREN booleanExpr RPAREN LBRACE topologyStatement* RBRACE
    ;

booleanExpr
    : expr relationalOperator expr
    | expr AND expr
    | expr OR expr
    | NOT expr
    ;

relationalOperator
    : EQUAL
    | NOT_EQUAL
    | LESS
    | GREATER
    | LESS_EQUAL
    | GREATER_EQUAL
    ;

// While statement
whileStatement
    : WHILE conditionWithBlock
    ;

// Do while statement
doWhileStatement
    : DO LBRACE topologyStatement* RBRACE WHILE LPAREN booleanExpr RPAREN SEMICOLON
    ;

// For statement
forStatement
    : FOR LPAREN forInit? SEMICOLON booleanExpr SEMICOLON forUpdate? RPAREN LBRACE topologyStatement* RBRACE
    ;

forInit
    : letAssignment
    | assignmentStatement
    ;

forUpdate
    : assignmentStatement
    ;

// Switch statement
switchStatement
    : SWITCH LPAREN expr RPAREN LBRACE caseStatement* defaultStatement? RBRACE
    ;

caseStatement
    : CASE expr COLON topologyStatement*
    ;

defaultStatement
    : DEFAULT COLON topologyStatement*
    ;

// Function definition
functionDefinition
    : FN ID LPAREN functionParams? RPAREN LBRACE functionBody RBRACE
    ;

functionParams
    : functionParam (COMMA functionParam)*
    ;

functionParam
    : ID (ASSIGN expr)?
    ;

functionBody
    : topologyStatement* returnStatement
    ;

returnStatement
    : RETURN expr SEMICOLON
    ;

// Subcircuit definition
subcircuitDefinition
    : SUBCIRCUIT ID LPAREN subcircuitParams? RPAREN COLON nodeList LBRACE topologyStatement* RBRACE
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