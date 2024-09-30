# tests/test_lexer.py
import unittest
from lexer import Lexer, TOKEN_PRINT, TOKEN_STRING

class TestLexer(unittest.TestCase):
    def test_tokenize_print(self):
        code = 'PRINT "Hello, World!"'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        self.assertEqual(tokens[0][0], TOKEN_PRINT)
        self.assertEqual(tokens[1][0], TOKEN_STRING)
        self.assertEqual(tokens[1][1], 'Hello, World!')

if __name__ == '__main__':
    unittest.main()
