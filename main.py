from lexer import Lexer
from parser import Parser
from codegen import CodeGen
import os

fname = "file.hung"
with open(fname) as f:
    text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

codegen = CodeGen()

module = codegen.module
builder = codegen.builder
printf = codegen.printf

pg = Parser(module, builder, printf)
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

codegen.create_ir()
codegen.save_ir("output/output.ll")
path = os.popen('pwd').read()
os.system('cd ' + str(path).split('\n')[0]+'/output && llc -filetype=obj output.ll && gcc output.o -o output')


