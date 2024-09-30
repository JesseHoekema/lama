# tests/test_parser.py
import unittest
from parser import Parser
from lexer import Lexer

class TestParser(unittest.TestCase):
    def test_parse_print(self):
        code = 'PRINT "Hello, World!"'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        program = parser.parse()
        self.assertEqual(program[0][0], 'PRINT')
        self.assertEqual(program[0][1], 'Hello, World!')

    def test_parse_add(self):
        code = 'ADD 5 + 3'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        program = parser.parse()
        self.assertEqual(program[0][0], 'ADD')
        self.assertEqual(program[0][1], 5)
        self.assertEqual(program[0][2], 3)

if __name__ == '__main__':
    unittest.main()
