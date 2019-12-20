from lexer import Lexer
from parser import Parser

text_input = '100+100-20+5*9'

lexer = Lexer()
tokens = lexer.get_tokens(text_input)

print(Parser().get_parser().parse(tokens).eval())

