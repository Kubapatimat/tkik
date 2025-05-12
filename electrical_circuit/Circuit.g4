grammar Circuit;

circuit: statement* EOF;

statement:
    componentDeclaration          // - opis komponentu elektronicznego (R1 = 10kOhm)
    | connection                    // - wizualne połączenia elementów V1 -> V2
    | modelDeclaration              // - linia opisująca diody, modele tranzystora itd.
    | simulationCommand             // - polecenie przepwadzenia symulacji .tran 1n 10u
    | NEWLINE
    ;
//Tutaj forma komponent + 2 wezly + wartosc + jednostka R1 n1 n2 10kOhm // Druga opcja to Przypisanie komponent = wartosc + jednostka R1 = 10Ohm
componentDeclaration : IDENTIFIER nodeList? valueWithUnit | IDENTIFIER ASSIGN valueWithUnit;
nodeList: IDENTIFIER+;

//Polaczenia V1->V2
connection: IDENTIFIER (ARROW IDENTIFIER)+;

//Wartosc z jednostka
valueWithUnit: value unit;
value: NUMBER (scaleFactor)?;

//scaleFactor - przedrostki jednostek
scaleFactor: 'p' | 'n' | 'u' | 'm' | 'k' | 'meg' | 'g' ;

unit: 'Ohm' | 'V' | 'A' | 'F' | 'H' | 'S' | 'W' | 'uF' | 'uH';

//Definicja modelu
modelDeclaration: '.model' IDENTIFIER IDENTIFIER '(' modelParamList? ')';
modelParamList: modelParam (WS+ modelParam)* ;
modelParam: IDENTIFIER ASSIGN value;

//symulacje .tran - symulacja w czasie , .dc symulacja napiecia
simulationCommand: '.tran' value (value)? | '.dc' IDENTIFIER value value value;

//Tutaj będa tokeny leksykalne
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+('.'[0-9]+)?;
ASSIGN: '=';
ARROW: '->';
NEWLINE:[\r\n]+ ;
WS:[ \t]+ -> skip ; //Wcięcia obecnie nie maja znaczenia
COMMENT: '//' ~[\r\n]* -> skip ;

//Rysowanie
COORDINATE          : [0-9]+ ('.' [0-9]+)?;
COORDINATES         : '('COORDINATE','COORDINATE')';
LPARENT             : '(';
RPARENT             : ')';