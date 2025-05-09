import pytest

from .lexer import Lexer, InvalidCharacterException
from .tokens import TokenType, Token


def test_lexer_valid_expression():
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


def test_lexer_invalid_character():
    lexer = Lexer("1+2+3 / (4 + 5) + 2^3 - 5! / 2")

    tokens = []
    with pytest.raises(InvalidCharacterException):
        while True:
            token = lexer.token()
            tokens.append(token)
            if token.token_type == TokenType.EOF:
                break


def test_lexer_invalid_identifier():
    test_data = "12 + abc * 3 + 4a - 5"
    lexer = Lexer(test_data)
    with pytest.raises(InvalidCharacterException) as error_info:
        while True:
            token = lexer.token()
            if token.token_type == TokenType.EOF:
                break
    error_message = str(error_info.value)
    assert "Identifier cannot start with a digit" in error_message


def test_lexer_unmatched_opening_parenthesis():
    lexer = Lexer("1 + 2 + (3 + 4")
    tokens = []
    with pytest.raises(InvalidCharacterException) as error_info:
        while True:
            token = lexer.token()
            tokens.append(token)
            if token.token_type == TokenType.EOF:
                break
    error_message = str(error_info.value)
    assert "Unmatched opening parenthesis" in error_message


def test_lexer_unmatched_closing_parenthesis():
    lexer = Lexer("(1 + 2) + 3) + 4")
    tokens = []
    with pytest.raises(InvalidCharacterException) as error_info:
        while True:
            token = lexer.token()
            tokens.append(token)
            if token.token_type == TokenType.EOF:
                break
    error_message = str(error_info.value)
    assert "Unmatched closing parenthesis" in error_message


def test_lexer_multiline_valid():
    lexer = Lexer("1 + 2\n+ 3")
    tokens = []
    while True:
        token = lexer.token()
        tokens.append(token)
        if token.token_type == TokenType.EOF:
            break
    assert tokens == [
        Token(TokenType.NUMBER, '1'),
        Token(TokenType.PLUS, '+'),
        Token(TokenType.NUMBER, '2'),
        Token(TokenType.PLUS, '+'),
        Token(TokenType.NUMBER, '3'),
        Token(TokenType.EOF, '')
    ]


def test_lexer_error_position():
    lexer = Lexer("1 + 2\n+ 3a + 4\n+ 5")
    tokens = []
    with pytest.raises(InvalidCharacterException) as error_info:
        while True:
            token = lexer.token()
            tokens.append(token)
            if token.token_type == TokenType.EOF:
                break
    error_message = str(error_info.value)
    assert "line 2, column 4" in error_message
    assert "Invalid character 'a'" in error_message


def test_lexer_valid_multiline_expression():
    lexer = Lexer("(1+2)\n*(3+4)\n /   (5 + 6) + abcd01\n\n\n - (2^3)^(-1)")
    tokens = []
    while True:
        token = lexer.token()
        tokens.append(token)
        if token.token_type == TokenType.EOF:
            break
    assert tokens == [
        Token(TokenType.LPAREN, '('),
        Token(TokenType.NUMBER, '1'),
        Token(TokenType.PLUS, '+'),
        Token(TokenType.NUMBER, '2'),
        Token(TokenType.RPAREN, ')'),
        Token(TokenType.MULTIPLY, '*'),
        Token(TokenType.LPAREN, '('),
        Token(TokenType.NUMBER, '3'),
        Token(TokenType.PLUS, '+'),
        Token(TokenType.NUMBER, '4'),
        Token(TokenType.RPAREN, ')'),
        Token(TokenType.DIVIDE, '/'),
        Token(TokenType.LPAREN, '('),
        Token(TokenType.NUMBER, '5'),
        Token(TokenType.PLUS, '+'),
        Token(TokenType.NUMBER, '6'),
        Token(TokenType.RPAREN, ')'),
        Token(TokenType.PLUS, '+'),
        Token(TokenType.IDENTIFIER, 'abcd01'),
        Token(TokenType.MINUS, '-'),
        Token(TokenType.LPAREN, '('),
        Token(TokenType.NUMBER, '2'),
        Token(TokenType.EXPONENT, '^'),
        Token(TokenType.NUMBER, '3'),
        Token(TokenType.RPAREN, ')'),
        Token(TokenType.EXPONENT, '^'),
        Token(TokenType.LPAREN, '('),
        Token(TokenType.MINUS, '-'),
        Token(TokenType.NUMBER, '1'),
        Token(TokenType.RPAREN, ')'),
        Token(TokenType.EOF, '')
    ]
