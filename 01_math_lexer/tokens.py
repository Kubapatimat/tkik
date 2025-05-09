from enum import Enum, auto


class TokenType(Enum):
    EOF = auto()
    NUMBER = auto()
    IDENTIFIER = auto()
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    EXPONENT = auto()
    LPAREN = auto()
    RPAREN = auto()


token_mapping = {
    "+": TokenType.PLUS,
    "-": TokenType.MINUS,
    "*": TokenType.MULTIPLY,
    "/": TokenType.DIVIDE,
    "^": TokenType.EXPONENT,
    "(": TokenType.LPAREN,
    ")": TokenType.RPAREN
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
