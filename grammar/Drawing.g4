// $antlr-format alignTrailingComments true, columnLimit 150, minEmptyLines 1, maxEmptyLinesToKeep 1, reflowComments false, useTab false
// $antlr-format allowShortRulesOnASingleLine false, allowShortBlocksOnASingleLine true, alignSemicolons hanging, alignColons hanging

grammar Draw;

// ========== PARSER RULES ==========

drawing
    : drawStmt* EOF
    ;

drawStmt
    : 'draw' componentType ID positionSpec annotation*
    ;

componentType
    : 'resistor'
    | 'capacitor'
    | 'inductor'
    | 'voltage_source'
    | 'current_source'
    | 'diode'
    | 'opamp'
    | 'transformer'
    | 'wire'
    | 'open'
    | 'short'
    ;

positionSpec
    : 'from' coordinate 'to' coordinate
    | 'at' coordinate
    ;

annotation
    : 'label' STRING
    | 'voltage' STRING
    | 'current' STRING
    ;

// ========== LEXER RULES ==========

ID
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

STRING
    : '"' (~["\\] | '\\' .)* '"'
    ;

fragment DIGIT
    : [0-9]
    ;

fragment SIGN
    : [+-]?
    ;

NUMBER
    : SIGN DIGIT+ ('.' DIGIT+)? // int or float
    ;

coordinate
    : '(' NUMBER ',' NUMBER ')'
    ;

WS
    : [ \t\r\n]+ -> skip
    ;