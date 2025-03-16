import pytest

from .lexer import Lexer, InvalidCharacterException
from .tokens import TokenType, Token

def test_lexer_valid():
    lexer = Lexer('2+3*(76+8/3)+ 3*(9-3)+10*abc01 -(a + b)')

    tokens = []
    while True:
        token = lexer.token()
        tokens.append(token)
        if token.token_type == TokenType.EOF:
            break

    assert tokens == [
        Token(TokenType.NUMBER, '2'),
        Token(TokenType.PLUS, '+'),
        Token(TokenType.NUMBER, '3'),
        Token(TokenType.MULTIPLY, '*'),
        Token(TokenType.LPAREN, '('),
        Token(TokenType.NUMBER, '76'),
        Token(TokenType.PLUS, '+'),
        Token(TokenType.NUMBER, '8'),
        Token(TokenType.DIVIDE, '/'),
        Token(TokenType.NUMBER, '3'),
        Token(TokenType.RPAREN, ')'),
        Token(TokenType.PLUS, '+'),
        Token(TokenType.NUMBER, '3'),
        Token(TokenType.MULTIPLY, '*'),
        Token(TokenType.LPAREN, '('),
        Token(TokenType.NUMBER, '9'),
        Token(TokenType.MINUS, '-'),
        Token(TokenType.NUMBER, '3'),
        Token(TokenType.RPAREN, ')'),
        Token(TokenType.PLUS, '+'),
        Token(TokenType.NUMBER, '10'),
        Token(TokenType.MULTIPLY, '*'),
        Token(TokenType.IDENTIFIER, 'abc01'),
        Token(TokenType.MINUS, '-'),
        Token(TokenType.LPAREN, '('),
        Token(TokenType.IDENTIFIER, 'a'),
        Token(TokenType.PLUS, '+'),
        Token(TokenType.IDENTIFIER, 'b'),
        Token(TokenType.RPAREN, ')'),
        Token(TokenType.EOF, '')
    ]

def test_lexer_invalid():
    lexer = Lexer("1+2+3 / (4 + 5) + 0ab")

    tokens = []
    with pytest.raises(InvalidCharacterException):
        while True:
            token = lexer.token()
            tokens.append(token)
            if token.token_type == TokenType.EOF:
                break