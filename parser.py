# parser.py

from lexer import (
    TOKEN_SAY, TOKEN_CALCULATE, TOKEN_NUMBER, TOKEN_STRING, TOKEN_EOF,
    TOKEN_ASK, TOKEN_IF, TOKEN_ELSE, TOKEN_EQUALS, TOKEN_IDENTIFIER
)

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
            elif self.current_token[0] == TOKEN_ASK:
                commands.append(self.parse_ask())
            elif self.current_token[0] == TOKEN_IF:
                commands.append(self.parse_if())
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

    def parse_ask(self):
        self.eat(TOKEN_ASK)
        token = self.current_token
        self.eat(TOKEN_STRING)  # The prompt message
        return ('ASK', token[1])

    def parse_if(self):
        self.eat(TOKEN_IF)
        
        # Left side can be either a string or an identifier (ASK variable)
        left = None
        if self.current_token[0] == TOKEN_IDENTIFIER:
            left = self.current_token[1]  # Store ASK variable name
            self.advance()
        elif self.current_token[0] == TOKEN_STRING:
            left = self.current_token[1]  # Store string value
            self.eat(TOKEN_STRING)
        else:
            raise ValueError(f"Expected STRING or IDENTIFIER, but got {self.current_token[0]}")
        
        self.eat(TOKEN_EQUALS)
        
        # Right side can be either a string or an identifier (ASK variable)
        right = None
        if self.current_token[0] == TOKEN_IDENTIFIER:
            right = self.current_token[1]  # Store ASK variable name
            self.advance()
        elif self.current_token[0] == TOKEN_STRING:
            right = self.current_token[1]  # Store string value
            self.eat(TOKEN_STRING)
        else:
            raise ValueError(f"Expected STRING or IDENTIFIER, but got {self.current_token[0]}")
        
        then_command = None
        else_command = None
        
        # Parse then command
        if self.current_token[0] == TOKEN_SAY:
            then_command = self.parse_say()
        elif self.current_token[0] == TOKEN_CALCULATE:
            then_command = self.parse_calculate()
            
        # Check for ELSE clause
        if self.current_token[0] == TOKEN_ELSE:
            self.advance()  # Skip ELSE token
            if self.current_token[0] == TOKEN_SAY:
                else_command = self.parse_say()
            elif self.current_token[0] == TOKEN_CALCULATE:
                else_command = self.parse_calculate()
        
        return ('IF', left, right, then_command, else_command)
