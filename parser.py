from rply import ParserGenerator
from ast import Add,Mul,Sub,Div,Number

class Parser:
    def __init__(self):
        pg = ParserGenerator(
            ['FLOAT', 'NUM', 'ADD', 'SUB', 'MUL', 'DIV', 'END','LPAREN','RPAREN'],
            precedence=[
                ('left', ['ADD', 'SUB']),
                ('left', ['MUL', 'DIV'])
            ]
        )
        @pg.production('expression : NUM')
        def expression_number(p):
            return Number(int(p[0].getstr()))

        @pg.production('expression : LPAREN expression RPAREN')
        def expression_parens(p):
            return p[1]

        @pg.production('expression : expression ADD expression')
        @pg.production('expression : expression SUB expression')
        @pg.production('expression : expression MUL expression')
        @pg.production('expression : expression DIV expression')
        def expression_binop(p):
            left = p[0]
            right = p[2]
            if p[1].gettokentype() == 'ADD':
                return Add(left, right)
            elif p[1].gettokentype() == 'SUB':
                return Sub(left, right)
            elif p[1].gettokentype() == 'MUL':
                return Mul(left, right)
            elif p[1].gettokentype() == 'DIV':
                return Div(left, right)
            else:
                raise AssertionError('Oops, this should not be possible!')
        self.pg = pg

    def get_parser(self):
        return self.pg.build()
