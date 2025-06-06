# main.py
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def main():
    with open("examples/ask_if_example.lama", "r") as file:
        code = file.read()

    lexer = Lexer(code)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    program = parser.parse()

    interpreter = Interpreter(program)
    interpreter.run()

if __name__ == '__main__':
    main()
