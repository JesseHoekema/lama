# run_lama.py
import sys
import os
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def run_lama_file(filename):
    try:
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found")
            return
            
        with open(filename, "r") as file:
            code = file.read()

        lexer = Lexer(code)
        tokens = lexer.tokenize()

        parser = Parser(tokens)
        program = parser.parse()

        interpreter = Interpreter(program)
        interpreter.run()
    except Exception as e:
        print(f"Error running program: {str(e)}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python lama_runner.py <filename.lama>")
        sys.exit(1)
    
    run_lama_file(sys.argv[1])
