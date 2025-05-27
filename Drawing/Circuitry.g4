grammar Circuitry;

circuit     : 'draw' '{' statement+ '}' EOF ;

statement   : component 'from' coord 'to' coord ';' ;

component   : 'resistor'
            | 'capacitor'
            | 'inductor'
            ;

coord       : '(' INT ',' INT ')' ;

INT         : [0-9]+ ;
WS          : [ \t\r\n]+ -> skip ;

