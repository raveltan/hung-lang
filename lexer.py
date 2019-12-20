import token
import error
import postition

DIGITS = '0123456789'

class Lexer:
    def __init__(self,file_name,text):
        self.text = text
        self.file_name = file_name
        self.position = postition.Position(-1,0,-1,file_name,text) 
        self.current_char = None
        self.next()

    def next(self):
        self.position.next(self.current_char)
        self.current_char = self.text[self.position.index] if self.position.index < len(self.text) else None

    def make_tokens(self):
        tokens:[token.Token] = []
        while not self.current_char == None:
            if self.current_char in ' \t':
                self.next()
            elif self.current_char in DIGITS:
                tokens.append(self.make_numbers())
            elif self.current_char == '+':
                tokens.append(token.Token(token.TT_ADD))
                self.next()
            elif self.current_char == '-':
                tokens.append(token.Token(token.TT_SUB))
                self.next()
            elif self.current_char == '*':
                tokens.append(token.Token(token.TT_MUL))
                self.next()
            elif self.current_char == '/':
                tokens.append(token.Token(token.TT_DIV))
                self.next()
            elif self.current_char == '(':
                tokens.append(token.Token(token.TT_OPEN_PAREN))
                self.next()
            elif self.current_char == ')':
                tokens.append(token.Token(token.TT_CLOSE_PAREN))
                self.next()
            else:
                position_start = self.position.copy()
                char = self.current_char
                self.next()
                return [],error.IllegalCharacterError(position_start,self.position,"'"+char+"'")

        return tokens,None

    def make_numbers(self):
        number_string = ''
        dot_count = 0
        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count+=1
                number_string += '.'
            else : number_string += self.current_char
            self.next()
        if dot_count == 0 : return token.Token(token.TT_NUM,int(number_string))
        else : return token.Token(token.TT_FLOAT,float(number_string))
