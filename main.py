import lexer
import termcolor
def run(text,file_name):
    return lexer.Lexer(file_name,text).make_tokens()

while True:
    text = input('HunG> ')
    result,error = run(text,'<HunG>')
    if error: print(error.to_string()[0],termcolor.colored(error.to_string()[1],'red'))
    else: print(result)