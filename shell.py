import lexer,parser,interpreter
import sys
import termcolor
import os

print(termcolor.colored('\nHunG 0.0.2 (www.github.com/raveltan, 26 Dec 2019)',color='cyan'))
print(f'Running on top of Python {sys.version}\n')
running = True
while running:
    data = input(termcolor.colored('HunG> ',color='cyan'))
    if data == '.clear': 
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    elif data == '.exit':
        running = False
        continue
    l = lexer.Lexer(data,'<HunGConsole>').get_tokens()
    if l[0] == None:
        print(l[1])
    else:
        #print(l[0])
        p = parser.Parser(l[0],'<HunGConsole>',data).parse()
        if p[0] == None:
            print(p[1])
        else:
            #print(p[0])
            i = interpreter.Interpreter(p[0],'<HunGConsole>',data).interpret()
            print(i)