from syntax.syntax_analysis import SyntaxAnalysis
from lexical.lexical_analysis import LexicalAnalysis
import unittest

def readCode(file):
    code = ''
    code = open(file, "r")
    code_content = list(code.read())
    code.close()
    return code_content

def includes(string, substring):
    return string.find(substring) > -1

class ConditionalExpressionsOperationsTests(unittest.TestCase):

    def test_should_pass_all_condition_cases(self):
        code_name = 'tests/tests_code/conditional_expressions_operations.c'
        code_content = readCode(code_name)
        al = LexicalAnalysis(code_name, code_content, output=False)
        error = ''

        try:
            SyntaxAnalysis(al).execute()
        except Exception as e:
            error = e.__str__()

        self.assertEqual(error, '')

    def test_should_raise_error_when_not_relational_operator(self):
        code_name = 'tests/tests_code/conditional_operator_error.c'
        code_content = readCode(code_name)
        al = LexicalAnalysis(code_name, code_content, output=False)
        error = ''

        try:
            SyntaxAnalysis(al).execute()
        except Exception as e:
            error = e.__str__()

        self.assertTrue(includes(error, 'relational operator Expected'))

    def test_should_raise_error_when_no_opening_parenthesis(self):
        code_name = 'tests/tests_code/conditional_parenthesis_error.c'
        code_content = readCode(code_name)
        al = LexicalAnalysis(code_name, code_content, output=False)
        error = ''

        try:
            SyntaxAnalysis(al).execute()
        except Exception as e:
            error = e.__str__()

        self.assertTrue(includes(error, 'opening Parenthesis Expected'))

    def test_should_raise_error_when_no_opening_parenthesis(self):
        code_name = 'tests/tests_code/conditional_else_without_curly_error.c'
        code_content = readCode(code_name)
        al = LexicalAnalysis(code_name, code_content, output=False)
        error = ''

        try:
            SyntaxAnalysis(al).execute()
        except Exception as e:
            error = e.__str__()

        self.assertTrue(includes(error, 'opening curly braces Expected'))

if __name__ == '__main__':
    unittest.main()

    