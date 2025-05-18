// $antlr-format alignTrailingComments true, columnLimit 150, maxEmptyLinesToKeep 1, reflowComments false, useTab false
// $antlr-format allowShortRulesOnASingleLine true, allowShortBlocksOnASingleLine true, minEmptyLines 0, alignSemicolons ownLine
// $antlr-format alignColons trailing, singleLineOverrulesHangingColon true, alignLexerCommands true, alignLabels true, alignTrailers true

lexer grammar CircuitryLexer;

// Brackets
LPAREN   : '(';
RPAREN   : ')';
LBRACE   : '{';
RBRACE   : '}';
LBRACKET : '[';
RBRACKET : ']';

// Math operators
PLUS     : '+';
MINUS    : '-';
MULTIPLY : '*';
DIVIDE   : '/';
MODULO   : '%';
EXPONENT : '^';

// Component and node operators
DOT    : '.';
RARROW : '->';

// Relational operators
EQUAL         : '==';
NOT_EQUAL     : '!=';
LESS          : '<';
GREATER       : '>';
LESS_EQUAL    : '<=';
GREATER_EQUAL : '>=';

// Assignment operators
ASSIGN     : '=';
ADD_ASSIGN : '+=';
SUB_ASSIGN : '-=';
MUL_ASSIGN : '*=';
DIV_ASSIGN : '/=';
MOD_ASSIGN : '%=';
EXP_ASSIGN : '^=';
INC        : '++';
DEC        : '--';

// Logical operators
AND : '&&';
OR  : '||';
NOT : '!';

// Delimiters
SEMICOLON : ';';
COLON     : ':';
COMMA     : ',';

// Keywords
ALIAS : 'alias';
LET   : 'let';

// Functions
FN     : 'fn';
RETURN : 'return';

// Connection types
SERIES   : 'series';
PARALLEL : 'parallel';
REVERSED : 'reversed';

// Subcircuit
SUBCIRCUIT: 'subcircuit';

// Imports
IMPORT: 'import';

// Conditional statements
IF   : 'if';
ELSE : 'else';

// Loops
FOR      : 'for';
WHILE    : 'while';
DO       : 'do';
BREAK    : 'break';
CONTINUE : 'continue';

// Switch-case
SWITCH  : 'switch';
CASE    : 'case';
DEFAULT : 'default';

// Logical values
TRUE  : 'true';
FALSE : 'false';

// Simulation directives
TRANSIENT : 'transient';
AC        : 'ac';
DC        : 'dc';

// Measurement directives
MEASURE: 'measure';

// Drawing directives
POS: 'pos';

// Floating point literals with underscore support
fragment Digit                 : [0-9];
fragment DigitsWithUnderscores : (Digit | '_')+;
fragment Digits                : Digit (DigitsWithUnderscores? Digit)?;

fragment ExponentPart      : ExponentIndicator SignedInteger;
fragment ExponentIndicator : [eE];
fragment SignedInteger     : Sign? Digits;
fragment Sign              : [+-];
fragment UnitPrefix        : [fpnu\u03BCmkKMGTP];

FLOAT_LITERAL:
    Sign? Digits '.' Digits? ExponentPart? UnitPrefix?
    | Sign? Digits ExponentPart UnitPrefix?
    | Sign? Digits UnitPrefix?
;

// String literals
STRING_LITERAL: '"' (~["\\] | '\\' .)*? '"';

// Identifiers
fragment NonDigit: [a-zA-Z_];

ID: NonDigit (NonDigit | Digit)*;

// Comments & whitespace
LINE_COMMENT      : '//' ~[\r\n]* -> skip;
MULTILINE_COMMENT : '/*' .*? '*/' -> skip;
WS                : [ \t\r\n]+    -> skip;