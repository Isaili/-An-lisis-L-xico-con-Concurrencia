import unittest
from src.lexer import Lexer

class TestLexer(unittest.TestCase):
    def test_identifiers(self):
        lexer = Lexer("var1 x")
        tokens = lexer.tokenize()
        self.assertEqual(tokens, [('IDENTIFIER', 'var1'), ('IDENTIFIER', 'x')])

    def test_numbers(self):
        lexer = Lexer("123 45.67")
        tokens = lexer.tokenize()
        self.assertEqual(tokens, [('NUMBER', '123'), ('FLOAT', '45.67')])

if __name__ == '__main__':
    unittest.main()
