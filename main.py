import lexer
def run(text,file_name):
    return lexer.Lexer(file_name,text).make_tokens()

while True:
    text = input('HunG> ')
    result,error = run(text,'<stdin>')
    if error: print(str(error))
    else: print(result)