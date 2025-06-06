# lexer.py
import re

# Token types
TOKEN_SAY = 'SAY'
TOKEN_CALCULATE = 'CALCULATE'
TOKEN_NUMBER = 'NUMBER'
TOKEN_STRING = 'STRING'
TOKEN_ASK = 'ASK'
TOKEN_IF = 'IF'
TOKEN_ELSE = 'ELSE'
TOKEN_EQUALS = 'EQUALS'
TOKEN_IDENTIFIER = 'IDENTIFIER'
TOKEN_EOF = 'EOF'

class Lexer:
    def __init__(self, input_code):
        self.input_code = input_code if input_code else ""
        self.position = 0
        self.current_char = self.input_code[self.position] if len(self.input_code) > 0 else None

    def advance(self):
        self.position += 1
        if self.position < len(self.input_code):
            self.current_char = self.input_code[self.position]
        else:
            self.current_char = None

    def peek(self):
        peek_pos = self.position + 1
        if peek_pos >= len(self.input_code):
            return None
        return self.input_code[peek_pos]

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
            elif self.current_char == '=':
                tokens.append((TOKEN_EQUALS, '='))
                self.advance()
            elif self.input_code.startswith('ASK', self.position):
                # Check if this is followed by a number (ASK1, ASK2, etc.)
                pos = self.position + 3
                if pos < len(self.input_code) and self.input_code[pos].isdigit():
                    tokens.append((TOKEN_IDENTIFIER, 'ASK' + self.input_code[pos]))
                    self.advance_by(4)
                else:
                    tokens.append((TOKEN_ASK, 'ASK'))
                    self.advance_by(3)
            elif self.input_code.startswith('SAY', self.position):
                tokens.append((TOKEN_SAY, 'SAY'))
                self.advance_by(3)
            elif self.input_code.startswith('IF', self.position):
                tokens.append((TOKEN_IF, 'IF'))
                self.advance_by(2)
            elif self.input_code.startswith('ELSE', self.position):
                tokens.append((TOKEN_ELSE, 'ELSE'))
                self.advance_by(4)
            elif self.input_code.startswith('CALCULATE', self.position):
                tokens.append((TOKEN_CALCULATE, 'CALCULATE'))
                self.advance_by(9)
            else:
                self.advance()  # Skip unknown characters
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

    def identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalpha() or self.current_char.isdigit()):
            result += self.current_char
            self.advance()
        return result
