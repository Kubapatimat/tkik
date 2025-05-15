parser grammar Draw;

options { tokenVocab=CommonRules; }

component
    : typename ID 'from' point 'to' point edge_modifier? anchor? label? current? voltage?
    ;

opamp
    : 'opamp' ID 'at' point
    ;

typename
    : 'resistor'
    | 'capacitor'
    | 'inductor'
    | 'voltage_source'
    | 'current_source'
    | 'wire'
    | 'diode'
    | 'transformer'
    | 'short'
    | 'open'
    ;

point
    : '(' NUMBER ',' NUMBER ')'
    ;

anchor_symbol
    : '*'
    | 'o'
;

edge_modifier
    : anchor_symbol? '-' anchor_symbol?
;

direction
    : '++' point
;

label: 'label' STRING;
current: 'current' STRING;
voltage: 'voltage' STRING;
anchor: 'anchor' STRING;
