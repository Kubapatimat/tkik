grammar Circuit;

circuit: statement+ EOF ;

statement
    : assignment NEWLINE?
    | connection NEWLINE?
    ;
assignment: IDENTIFIER ASSIGN value; //Tutaj mamy przypisanie
connection: IDENTIFIER (ARROW IDENTIFIER)+; //Tutaj mamy Połaczenie V1 -> R1
value: NUMBER UNIT; //Tutaj mamy wartości z jednostką na przykład 5V

//Tutaj będa tokeny leksykalne
IDENTIFIER : [A-Za-z_][A-Za-z0-9_]*;
NUMBER: [0-9]+('.'[0-9]+)?;
ASSIGN: '=';
ARROW: '->';
UNIT: 'Ohm' | 'V' | 'A' | 'F' | 'H' | 'uF' | 'mH';
NEWLINE:[\r\n]+ ;
WS:[ \t]+ -> skip ;