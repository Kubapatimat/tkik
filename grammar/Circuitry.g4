grammar Circuitry;

circuit
    : statement* EOF
    ;

statement
    : letStmt
    | componentStmt
    | subcircuitDecl
    | subcircuitInst
    | macroStmt
    | namedMacroStmt
    | functionDecl
    | returnStmt
    | analysisStmt
    ;

letStmt
    : LET assignment (',' assignment)*
    ;
assignment
    : ID '=' expr
    ;

componentStmt
    : ID '=' expr ':' nodeList
    ;
subcircuitDecl
    : SUBCIRCUIT ID '(' paramList? ')' ':' nodeList block
    ;
paramList
    : assignment (',' assignment)*
    ;

subcircuitInst
    : ID '=' ID '(' argList? ')' ':' (mappingList | nodeList)
    ;
argList
    : assignment (',' assignment)*
    ;

mappingList
    : mapping (',' mapping)*
    ;
mapping
    : ID '->' ID
    ;

macroStmt
    : (SERIES | PARALLEL) (':' nodeList)? block
    ;


namedMacroStmt
    : ID '=' (SERIES | PARALLEL) (':' nodeList)? block
    ;

block
    : '{' statement* '}'
    ;

analysisStmt
    : TRANSIENT '(' expr ')'
    | OP
    ;


functionDecl
    : FN ID '(' paramIDList? ')' block
    ;
paramIDList
    : ID (',' ID)*
    ;


returnStmt
    : RETURN expr
    ;


// Expr rules
expr
    : expr op=('*'|'/') expr
    | expr op=('+'|'-') expr
    | ID '(' argList? ')'
    | NUMBER
    | elementRef
    | ID
    | '(' expr ')'
    ;
nodeList
    : node (',' node)*
    ;
node
    : ID
    ;


elementRef
    : '{' ID '}'
    ;


// Lexer tokens


BLOCK_COMMENT
    : '/**' .*? '*/' -> skip
    ;

COMMENT
    : '#' ~[\r\n]* -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

// keywords
LET         : 'let';
SUBCIRCUIT  : 'subcircuit';
SERIES      : 'series';
PARALLEL    : 'parallel';
TRANSIENT   : 'transient';
OP          : 'op';


FN          : 'fn';
RETURN      : 'return';

// liczby z sufiksem jednostki (k, m, μ, M, G, T, itd.)
NUMBER
    : DIGIT+ ('.' DIGIT+)? [a-zA-Zμ]*
    ;

// identyfikatory
ID
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

// fragment dla cyfr
fragment DIGIT
    : [0-9]
    ;
