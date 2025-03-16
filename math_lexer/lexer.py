from .tokens import TokenType, Token
from .utils import is_whitespace, is_digit, is_alpha

class InvalidCharacterException(Exception):
    pass

class Lexer:
    def __init__(self, data: str):
        self.pos = 0
        self.data = data

    def token(self) -> Token:
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
            self.pos += 1
            while self.pos < len(self.data) and is_digit(self.data[self.pos]):
                self.pos += 1
            return Token(TokenType.NUMBER, self.data[start:self.pos])
        if is_alpha(char):
            start = self.pos
            self.pos += 1
            while self.pos < len(self.data) and (is_alpha(self.data[self.pos]) or is_digit(self.data[self.pos])):
                self.pos += 1
            return Token(TokenType.IDENTIFIER, self.data[start:self.pos])
        else:
            raise InvalidCharacterException(f'Invalid character at position {self.pos}: {char}')