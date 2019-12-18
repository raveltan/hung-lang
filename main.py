from lexer import Lexer
from parser import Parser

lexer = Lexer().get_lexer()
while True:
    text_input = (input('Hung >'))
    tokens = lexer.lex(text_input)

    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    parser.parse(tokens).eval()