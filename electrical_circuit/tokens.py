from enum import Enum, auto


class TokenType(Enum):
    EOF = auto()              # end of file
    IDENTIFIER = auto()       # ex. name of component: R1, C1
    NUMBER = auto()           # numbers
    ASSIGN = auto()           # = (assign value ex. Resistance = 10Ohm)
    ARROW = auto()            # -> (connect with direction)
    CONNECTION = auto()       # -- (connect without direction)
    UNIT = auto()             # Ohm, V, A, F, H
    NODE = auto()             # GND, n1, IN, OUT
    NEWLINE = auto()          # \n

token_mapping = {
    "=": TokenType.ASSIGN,
    "->": TokenType.ARROW,
    "--": TokenType.CONNECTION,
}



class Token:
    def __init__(self, token_type: TokenType, value: str, start_pos: int = None, end_pos: int = None):
        self.token_type = token_type
        self.value = value
        self.start_pos = start_pos
        self.end_pos = end_pos

    def __repr__(self):
        return f'{self.token_type.name}, {self.value}'

    def __eq__(self, other):
        return self.token_type == other.token_type and self.value == other.value

# example of use
# V1 = 5V
# R1 = 100Ohm
# V1 -> R1 -> GND
