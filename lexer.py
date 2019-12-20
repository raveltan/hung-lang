import rply

class Lexer:
    def __init__(self):
        self.lg = rply.LexerGenerator()
        self.__add_tokens()
    #Add tokens that can be read by the lexer
    def __add_tokens(self):
        #Add all digits as a token
        self.lg.add('NUM',r'\d+')
        #Add binary operators as a token
        self.lg.add('ADD',r'\+')
        self.lg.add('SUB',r'\-')
        self.lg.add('MUL',r'\*')
        self.lg.add('DIV',r'\/')
        #ignore white spaces from being tokenized
        self.lg.ignore(r'\s+')
        #Add semicolon as end of statement
        self.lg.add('END',r'\;')
        #Add parentheses as a token
        self.lg.add('LPAREN',r'\(')
        self.lg.add('RPAREN',r'\)')
        #Add curly braces as a token
        self.lg.add('LCURLY',r'\{')
        self.lg.add('RCURLY',r'\}')
        #Add binary logical operator
        self.lg.add('AND',r'\&')
        self.lg.add('OR',r'\|')
        self.lg.add('XOR',r'\^')
        #Add unary operator
        self.lg.add('NOT',r'not')
        #Add main builtin function
        self.lg.add('LOG',r'log')
    #Retern the lexed tokens
    def get_tokens(self,text):
        return self.lg.build().lex(text)
