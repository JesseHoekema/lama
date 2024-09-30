# parser.py

from lexer import TOKEN_SAY, TOKEN_CALCULATE, TOKEN_NUMBER, TOKEN_STRING, TOKEN_EOF

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[self.position]

    def advance(self):
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]

    def eat(self, token_type):
        if self.current_token[0] == token_type:
            self.advance()
        else:
            raise ValueError(f"Expected token {token_type}, but got {self.current_token[0]}")

    def parse(self):
        commands = []
        while self.current_token[0] != TOKEN_EOF:
            if self.current_token[0] == TOKEN_SAY:
                commands.append(self.parse_say())
            elif self.current_token[0] == TOKEN_CALCULATE:
                commands.append(self.parse_calculate())
            else:
                self.advance()  # Skip unrecognized tokens
        return commands

    def parse_say(self):
        self.eat(TOKEN_SAY)
        token = self.current_token
        self.eat(TOKEN_STRING)
        return ('SAY', token[1])

    def parse_calculate(self):
        self.eat(TOKEN_CALCULATE)  # Consume 'CALCULATE' token
        left = self.current_token[1]
        self.eat(TOKEN_NUMBER)  # Consume first number
        self.eat(TOKEN_CALCULATE)  # Consume '+' token
        right = self.current_token[1]
        self.eat(TOKEN_NUMBER)  # Consume second number
        return ('CALCULATE', left, right)
