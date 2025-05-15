grammar Circuitry;

import Draw;

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
    | drawStmt
    ;

//let a, b = wartość
letStmt
    : LET assignment (',' assignment)*
    ;

assignment
    : ID '=' expr
    ;
// Deklaracja elementu obwodu: nazwa = wyrażenie [: lista węzłów]
componentStmt
    : ID '=' expr (':' nodeList)?
    ;
//Definicja podobwodu: subcircuit NAZWA(parametry) : wejścia/wyjścia { ciało }
subcircuitDecl
    : SUBCIRCUIT ID '(' paramList? ')' ':' nodeList block
    ;
paramList
    : assignment (',' assignment)*
    ;
//Instancja podobwodu: alias = nazwaPodobwodu(argList) : mapowanie lub zwykłe węzły
subcircuitInst
    : ID '=' ID '(' argList? ')' ':' (mappingList | nodeList)
    ;
argList
    : (assignment | expr) (',' (assignment | expr))*
    ;

mappingList
    : mapping (',' mapping)*
    ;
mapping
    : ID '->' ID
    ;
//Anonimowy lub nazwana seria/równoległość elementów
macroStmt
  : (SERIES | PARALLEL) (':' nodeList)? block
  ;


namedMacroStmt
  : ID '=' (SERIES | PARALLEL) (':' nodeList)? block
  ;

//Blok kodu: { zero lub więcej zdań }
block
    : '{' statement* '}'
    ;
//Analiza transientna lub OP (operacje)
analysisStmt
    : TRANSIENT '(' expr ')'
    | OP
    ;

drawStmt
    : 'draw' component
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


//Reguły dla wyrażeń arytmetycznych i wywołań funkcji
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
    : (ID | NUMBER) ('.' ID | '.+' | '.-')*
    ;

//Odwołanie do elementu: {nazwa_elementu}
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

//identyfikatory
ID
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

//fragment dla cyfr
fragment DIGIT
    : [0-9]
    ;
