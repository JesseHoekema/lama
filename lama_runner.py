# run_lama.py
import sys
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def run_lama_file(filename):
    # Lees de code uit het .lama-bestand
    with open(filename, "r") as file:
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
    if len(sys.argv) != 2:
        print("Usage: python run_lama.py <filename.lama>")
        sys.exit(1)

    run_lama_file(sys.argv[1])
