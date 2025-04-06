DIGITS = '0123456789'
WHITESPACE = ' \t\r\f\v'


def is_digit(char: str) -> bool:
    return char in DIGITS


def is_whitespace(char: str) -> bool:
    return char in WHITESPACE


def is_alpha(char: str) -> bool:
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z' or char == '_'


__all__ = ['is_digit', 'is_whitespace', 'is_alpha']