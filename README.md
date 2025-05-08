# Język do opisu i analizy obwodów elektrycznych

## Autorzy:
- Jakub Halfar - jakubhalfar@student.agh.edu.pl
- Aleksander Pyrdek - apyrdek@student.agh.edu.pl
- Antoni Pater - antonipater@student.agh.edu.pl

## Załóżenia programu
Projekt ma na celu:
- Ułatwić **rozwiązywanie obwodów elektrycznych**
- Zapewnić **czytelną wizualizację układów**
- Wspierać **definicję składni komponentów** za pomocą parsera opartego na **ANTLR 4**



# Opis tokenów i gramatyki
Składnia będzie składała się z dwóch głównych sekcji:
- Deklaracji komponentów oraz ich własności
  component_name = attributes
- Węzłów (komponentów) oraz listy ich sąsiadów
  component_name, {nodes_connected}

<pre>
Basic electrical tokens:
V         ; Voltage  
I         ; Current  
R         ; Resistance  
L         ; Inductance  
C         ; Capacitance  
G         ; Conductance  
Z         ; Impedance (complex)
</pre>

<pre>
Voltage & Current Source Waveforms
DC       ; DC value
AC       ; AC magnitude and phase
PULSE    ; Pulse waveform
SINE     ; Sine waveform
EXP      ; Exponential waveform
PWL      ; Piecewise Linear waveform
</pre>

<pre>
Functions & Operators
time           ; Simulation time
TEMP           ; Simulation temperature
IF(cond, t, f) ; Conditional expression
ABS(x)         ; Absolute value
SIN(x)         ; Sine function
COS(x)         ; Cosine function
EXP(x)         ; Exponential
LN(x)          ; Natural log
LOG(x)         ; Log base 10
SQRT(x)        ; Square root
TABLE(x, ...)  ; Lookup table
U(x)           ; Unit step function
</pre>

* Przykładowy układ RC zasilany napięciem pulsacyjnym
<pre>
V1 {R1, C1}
R1 {V1, C1}
C1 {R1, V1}

V1 = PULSE(0 5 0 1n 1n 10u 20u)
R1 = 1k
C1 = 10u

+------[R1]------[C1]-----+
|                         |
[V1]                     GND
|                         |
+-------------------------+

</pre>




