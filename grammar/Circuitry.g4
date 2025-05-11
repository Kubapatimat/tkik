grammar Circuitry;
circuit
    : statement* EOF;

statement
    : letStmt
    | componentStmt
    | subcircuitDecl
    | subcircuitInst
    | macroStmt
    | analysisStmt
    ;

letStmt
    : LET assignment(',' assignment)*
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
block
    : '{' statement* '}'
    ;

analysisStmt
    : TRANSIENT '(' expr ')'
    | OP
    ;

// expr rules

expr
    : expr op=('*'|'/') expr
    | expr op=('+'|'-') expr
    | ID '(' argList? ')'
    | NUMBER
    | ID
    | '(' expr ')'
    ;
nodeList
    : node (',' node)*
    ;
node
    : ID
    ;

//Tokens
LET : 'let';
SUBCIRCUIT : 'subcircuit';
SERIES : 'series';
PARALLEL : 'parallel';
TRANSIENT : 'transient';
OP : 'op';

//libcza z czescia dziesietna opcjonalnie i suffix jednostki
NUMBER
    : DIGIT+ ('.' DIGIT+)? [a-zA-Zμ]*
    ;
ID
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;
COMMENT : '#' ~[\r\n]* -> skip;

WS : [ \t\r\n]+ -> skip;

fragment DIGIT : [0-9];
