# main.py

from lexer import Lexer
from tokens import TokenType


def generate_html(tokens):
    token_styles = {
        TokenType.KEYWORD: 'color: blue; font-weight: bold;',
        TokenType.IDENTIFIER: 'color: black;',
        TokenType.NUMBER: 'color: darkorange;',
        TokenType.STRING: 'color: darkgreen;',
        TokenType.COMMENT: 'color: gray; font-style: italic;',
        TokenType.OPERATOR: 'color: red;',
        TokenType.DELIMITER: 'color: purple;',
        TokenType.WHITESPACE: ''
    }

    html_output = "<!DOCTYPE html>\n<html>\n<head>\n<meta charset='UTF-8'>\n"
    html_output += "<title>Pokolorowany kod Python</title>\n<style>\n"
    html_output += "pre { font-family: Consolas, monospace; font-size: 14px; }\n"
    for token_type, style in token_styles.items():
        if style:
            html_output += f".{token_type.name.lower()} " + "{ " + style + " }\n"
    html_output += "</style>\n</head>\n<body>\n<pre>\n"

    for token in tokens:
        if token.token_type == TokenType.EOF:
            continue
        #Tutaj zabezpieczone są znaki html - w celu unikniecia błędów
        token_val = (token.value
                     .replace('&', '&amp;')
                     .replace('<', '&lt;')
                     .replace('>', '&gt;'))
        if token.token_type == TokenType.WHITESPACE:
            html_output += token_val  # tutaj jest wypiswanie białych znaków bez span
        else:
            html_output += f'<span class="{token.token_type.name.lower()}">{token_val}</span>'
    html_output += "\n</pre>\n</body>\n</html>"
    return html_output


def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        code = f.read()
    lexer = Lexer(code)
    tokens = lexer.tokenize_all()
    html_result = generate_html(tokens)

    with open('output.html', 'w', encoding='utf-8') as f:
        f.write(html_result)

    print("Plik został zapisany")


if __name__ == '__main__':
    main()
