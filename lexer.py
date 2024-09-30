# lexer.py
import re

# Token types
TOKEN_SAY = 'SAY'
TOKEN_CALCULATE = 'CALCULATE'
TOKEN_NUMBER = 'NUMBER'
TOKEN_STRING = 'STRING'
TOKEN_EOF = 'EOF'

class Lexer:
    def __init__(self, input_code):
        self.input_code = input_code
        self.position = 0
        self.current_char = self.input_code[self.position]

    def advance(self):
        self.position += 1
        if self.position < len(self.input_code):
            self.current_char = self.input_code[self.position]
        else:
            self.current_char = None

    def tokenize(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
            elif self.current_char.isdigit():
                tokens.append((TOKEN_NUMBER, self.integer()))
            elif self.current_char == '"':
                tokens.append((TOKEN_STRING, self.string()))
            elif self.current_char == '+':
                tokens.append((TOKEN_CALCULATE, '+'))
                self.advance()
            elif self.input_code.startswith('SAY', self.position):
                tokens.append((TOKEN_SAY, 'SAY'))
                self.advance_by(3)
            elif self.input_code.startswith('CALCULATE', self.position):
                tokens.append((TOKEN_CALCULATE, 'CALCULATE'))
                self.advance_by(9)
            else:
                raise ValueError(f"Unknown character: {self.current_char}")
        tokens.append((TOKEN_EOF, None))
        return tokens

    def advance_by(self, steps):
        for _ in range(steps):
            self.advance()

    def integer(self):
        num = ''
        while self.current_char is not None and self.current_char.isdigit():
            num += self.current_char
            self.advance()
        return int(num)

    def string(self):
        result = ''
        self.advance()  # Skip opening quote
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()  # Skip closing quote
        return result
