from rply import LexerGenerator

class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()
    def __add_tokens(self):
        # Log
        self.lexer.add('LOG', r'log')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Ignore spaces
        self.lexer.ignore(r'\s+')
    def get_lexer(self):
        self.__add_tokens()
        return self.lexer.build()