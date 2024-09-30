# main.py
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def main():
    # Lees de code uit een voorbeeldbestand met .lama-extensie
    with open("examples/hello_world.lama", "r") as file:
        code = file.read()

    # Tokenize de code
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    # Parse de tokens in een programma (AST)
    parser = Parser(tokens)
    program = parser.parse()

    # Voer het programma uit met de interpreter
    interpreter = Interpreter(program)
    interpreter.run()

if __name__ == '__main__':
    main()
