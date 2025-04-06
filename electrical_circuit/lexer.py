from .tokens import Token, TokenType, token_mapping
from .utils import is_whitespace, is_digit, is_alpha


class InvalidCharacterException(Exception):
    pass


class Lexer:
    def __init__(self, data: str):
        self._pos = 0
        self._data = data
        self._line = 1
        self._column = 1

    def _is_within_bounds(self):
        return self._pos < len(self._data)

    def _peek(self, ahead=1):
        if self._pos + ahead < len(self._data):
            return self._data[self._pos + ahead]
        return ''

    def _advance(self):
        if self._data[self._pos] == '\n':
            self._line += 1
            self._column = 1
        else:
            self._column += 1
        self._pos += 1

    def _match(self, text):
        end = self._pos + len(text)
        return self._data[self._pos:end] == text

    def token(self):
        while self._is_within_bounds():
            char = self._data[self._pos]

            # whitespace(skip)
            if is_whitespace(char):
                self._advance()
                continue

            # newline (we need this so that we can add comments in our code ex. # first circuit)
            if char == '\n':
                token = Token(TokenType.NEWLINE, '\n', self._pos, self._pos)
                self._advance()
                return token

            # comments
            if char == '#':
                start = self._pos
                while self._is_within_bounds() and self._data[self._pos] != '\n':
                    self._advance()
                return Token(TokenType.COMMENT, self._data[start:self._pos], start, self._pos - 1)

            # arrow and connection
            if self._match('->'):
                token = Token(TokenType.ARROW, '->', self._pos, self._pos + 1)
                self._pos += 2
                self._column += 2
                return token
            if self._match('--'):
                token = Token(TokenType.CONNECTION, '--', self._pos, self._pos + 1)
                self._pos += 2
                self._column += 2
                return token

            # single-character tokens eg. =
            if char in token_mapping:
                token = Token(token_mapping[char], char, self._pos, self._pos)
                self._advance()
                return token

            # numbers (possibly with decimal or exponent)
            if is_digit(char):
                start = self._pos
                has_dot = False
                has_exp = False
                while self._is_within_bounds():
                    c = self._data[self._pos]
                    if c == '.' and not has_dot:
                        has_dot = True
                    elif c in 'eE' and not has_exp:
                        has_exp = True
                        self._advance()
                        if self._is_within_bounds() and self._data[self._pos] in '+-':
                            self._advance()
                        continue
                    elif not is_digit(c):
                        break
                    self._advance()
                return Token(TokenType.NUMBER, self._data[start:self._pos], start, self._pos - 1)

            # identifiers (component names, nodes, units)
            if is_alpha(char):
                start = self._pos
                while self._is_within_bounds() and (is_alpha(self._data[self._pos]) or is_digit(self._data[self._pos])):
                    self._advance()
                value = self._data[start:self._pos]

                # identifying units
                units = {'Ohm', 'V', 'A', 'F', 'H', 'uF', 'uH', 'kOhm', 'mA'}
                if value in units:
                    return Token(TokenType.UNIT, value, start, self._pos - 1)

                # nodes
                if value.upper() in {'GND', 'IN', 'OUT'} or value.startswith('n'):
                    return Token(TokenType.NODE, value, start, self._pos - 1)

                # component indentifier
                return Token(TokenType.IDENTIFIER, value, start, self._pos - 1)

            # unknown character
            raise InvalidCharacterException(
                f"Invalid character '{char}' at line {self._line}, column {self._column}."
            )

        return Token(TokenType.EOF, '', self._pos, self._pos)
