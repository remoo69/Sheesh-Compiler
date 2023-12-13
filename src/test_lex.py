import unittest
import lexerpy as lex

class TestLex(unittest.TestCase):
    
    def test_is_Text(self):
        tests=[
            "hello",
            "\"hello\"",
            """hello""",
            "'hello'"
        ]
        for test in tests:
            self.assertEqual(lex.is_Text(test), True)

if __name__=='__main__':
    unittest.main()