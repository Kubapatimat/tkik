from tokens import TokenType, Token, single_char_tokens
from utils import is_digit, is_whitespace, is_alpha

python_keywords = {
    "def", "class", "if", "else", "elif", "while", "for", "in", "try", "except",
    "finally", "with", "return", "import", "from", "as", "pass", "break", "continue",
    "and", "or", "not", "is", "None", "True", "False", "raise"
}

class Lexer:
    def __init__(self, data: str):
        self._data = data
        self._pos = 0
        self._line = 1
        self._column = 1

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
    def _peek(self, n=1):
        if self._pos + n < len(self._data):
            return self._data[self._pos + n]
        return ''

    def token(self):
        if not self._is_within_bounds():
            return Token(TokenType.EOF, '', self._pos, self._pos)
        char = self._data[self._pos]

        #tutaj jeest wazne bo wazne sa w pythonie taby - ilsoc bialych znaków
        if is_whitespace(char):
            start = self._pos
            while self._is_within_bounds() and is_whitespace(self._data[self._pos]):
                self._advance()
            return Token(TokenType.WHITESPACE, self._data[start:self._pos], start, self._pos - 1)
        #obsługa komentarzy
        if char == '#':
            start = self._pos
            while self._is_within_bounds() and self._data[self._pos] != '\n':
                self._advance()
            return Token(TokenType.COMMENT, self._data[start:self._pos], start, self._pos - 1)
        #Obsługa łańcucha znaków
        if char in ('"', "'"):
            quote_char = char
            start = self._pos
            self._advance()
            while self._is_within_bounds() and self._data[self._pos] != quote_char:
                if self._data[self._pos] == '\\':
                    self._advance()
                    if self._is_within_bounds():
                        self._advance()
                else:
                    self._advance()
            self._advance()
            return Token(TokenType.STRING, self._data[start:self._pos], start, self._pos - 1)
        #Obsługa liczb
        if is_digit(char):
            start = self._pos
            self._advance()
            while self._is_within_bounds() and is_digit(self._data[self._pos]):
                self._advance()
            if self._is_within_bounds() and self._data[self._pos] == '.':
                self._advance()
                while self._is_within_bounds() and is_digit(self._data[self._pos]):
                    self._advance()
            return Token(TokenType.NUMBER, self._data[start:self._pos], start, self._pos - 1)
        #Obsługa identyfikatorów oraz wywołanie funkcji
        if is_alpha(char):
            start = self._pos
            self._advance()
            while self._is_within_bounds() and (is_alpha(self._data[self._pos]) or is_digit(self._data[self._pos])):
                self._advance()
            value = self._data[start:self._pos]
            if value in python_keywords:
                return Token(TokenType.KEYWORD, value, start, self._pos - 1)
            if value == "self":
                return Token(TokenType.FUNCTION, value, start, self._pos - 1)
#Tutaj jest to sprawdzenie żeby oznaczyć funkcje
            if self._is_within_bounds() and self._data[self._pos] == '(':
                return Token(TokenType.FUNCTION, value, start, self._pos - 1)
            return Token(TokenType.IDENTIFIER, value, start, self._pos - 1)

        if char in single_char_tokens:
            token = Token(single_char_tokens[char], char, self._pos, self._pos)
            self._advance()
            return token

    def tokenize_all(self):
        tokens = []
        while True:
            tok = self.token()
            tokens.append(tok)
            if tok.token_type == TokenType.EOF:
                break
        return tokens
