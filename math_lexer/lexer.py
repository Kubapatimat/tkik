from .tokens import TokenType, Token
from .utils import is_whitespace, is_digit, is_alpha

class InvalidCharacterException(Exception):
    pass

class Lexer:
    def __init__(self, data: str):
        self.pos = 0
        self.data = data
        self.line, self.column = 1, 1
    def advance(self):
        if self.pos < len(self.data):
            if self.data[self.pos] == '\n':
                self.line+=1
                self.column = 1
            else:
                self.column+=1

        self.pos += 1

    def token(self) -> Token:
        while self.pos < len(self.data) and self.data[self.pos].isspace():
            self.advance()

        if self.pos >= len(self.data):
            return Token(TokenType.EOF, '', self.pos, self.pos)

        char = self.data[self.pos]
        if is_whitespace(char):
            self.pos += 1
            return self.token()
        if char == '+':
            token = Token(TokenType.PLUS, '+', self.pos, self.pos)
            self.pos += 1
            return token
        if char == '-':
            token = Token(TokenType.MINUS, '-', self.pos, self.pos)
            self.pos += 1
            return token
        if char == '*':
            token = Token(TokenType.MULTIPLY, '*', self.pos, self.pos)
            self.pos += 1
            return token
        if char == '/':
            token = Token(TokenType.DIVIDE, '/', self.pos, self.pos)
            self.pos += 1
            return token
        if char == '(':
            token = Token(TokenType.LPAREN, '(', self.pos, self.pos)
            self.pos += 1
            return token
        if char == ')':
            token = Token(TokenType.RPAREN, ')', self.pos, self.pos)
            self.pos += 1
            return token
        if is_digit(char):
            start = self.pos
            self.advance()
            while self.pos < len(self.data) and is_digit(self.data[self.pos]):
                self.advance()
            if self.pos < len(self.data) and is_alpha(self.data[self.pos]):
                raise InvalidCharacterException(
                    f"Invalid character '{self.data[self.pos]}' is number token at line {self.line}, column {self.column}"
                )
            return Token(TokenType.NUMBER, self.data[start:self.pos],start, self.pos-1)
        if is_alpha(char):
            start = self.pos
            self.advance()
            while self.pos < len(self.data) and (is_alpha(self.data[self.pos]) or is_digit(self.data[self.pos])):
                self.advance()
            return Token(TokenType.IDENTIFIER, self.data[start:self.pos], start, self.pos-1)
        else:
            raise InvalidCharacterException(f'Invalid character at line {self.line}, column {self.column}')