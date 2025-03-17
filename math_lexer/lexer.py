from .tokens import TokenType, Token, token_mapping
from .utils import is_whitespace, is_digit, is_alpha


class InvalidCharacterException(Exception):
    pass


class Lexer:
    def __init__(self, data: str):
        self._pos = 0
        self._data = data
        self._line = 1
        self._column = 1
        self._parentheses = 0

    def _is_within_bounds(self):
        return self._pos < len(self._data)

    def _advance(self):
        if self._pos < len(self._data):
            if self._data[self._pos] == '\n':
                self._line += 1
                self._column = 1
            else:
                self._column += 1

        self._pos += 1

    def token(self) -> Token:
        if not self._is_within_bounds():
            if self._parentheses:
                raise InvalidCharacterException(
                    f"Invalid character at line {self._line}, column {self._column}. "
                    f"Unmatched opening parenthesis."
                )
            return Token(TokenType.EOF, '', self._pos, self._pos)

        char = self._data[self._pos]
        if is_whitespace(char):
            self._advance()
            while self._is_within_bounds() and is_whitespace(self._data[self._pos]):
                self._advance()
            return self.token()
        if char in token_mapping:
            token = Token(token_mapping[char], char, self._pos, self._pos)
            self._advance()
            if char == '(':
                self._parentheses += 1
            elif char == ')':
                if self._parentheses == 0:
                    raise InvalidCharacterException(
                        f"Invalid character '{char}' at line {self._line}, column {self._column}. "
                        f"Unmatched closing parenthesis."
                    )
                self._parentheses -= 1
            return token
        if is_digit(char):
            start = self._pos
            self._advance()
            while self._is_within_bounds() and is_digit(self._data[self._pos]):
                self._advance()
            if self._is_within_bounds() and is_alpha(self._data[self._pos]):
                raise InvalidCharacterException(
                    f"Invalid character '{self._data[self._pos]}' at line {self._line}, column {self._column}. "
                    f"Identifier cannot start with a digit."
                )
            return Token(TokenType.NUMBER, self._data[start:self._pos], start, self._pos - 1)
        if is_alpha(char):
            start = self._pos
            self._advance()
            while self._is_within_bounds() and (is_alpha(self._data[self._pos]) or is_digit(self._data[self._pos])):
                self._advance()
            return Token(TokenType.IDENTIFIER, self._data[start:self._pos], start, self._pos - 1)
        else:
            raise InvalidCharacterException(
                f"Invalid character '{char}' at line {self._line}, column {self._column}.")
