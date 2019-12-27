#imports
import error
import string

#Const
T_NUM = 'NUM'
T_STR = 'STRING'

K_LPAREN = 'LPAREN'
K_RPAREN = 'RPAREN'
K_END = 'END'
K_ADD = 'ADD'
K_EQUAL = 'EQUAL'
K_MIN = 'MIN'
K_MUL = 'MUL'
K_DIV = 'DIV'
K_IDENTIFIER = 'IDENTIFIER'
K_KEYWORD = 'KEYWORD'

K_RESERVED = [
    'var'
] 

F_LOG = 'LOG'

S_EOF = 'EOF'



#Token
class Token:
    def __init__(self, data_type,value,start):
        self.data_type = data_type
        self.start = start
        self.value = value
    def __repr__(self):
        return f'Token({self.data_type},{self.value})'

#Lexer
class Lexer:
    def __init__(self,text:str,file_name):
        self.line = 1 #TODO: FIX MULTILINE SUPPORT
        self.file_name = file_name
        self.raw = text
        self.position = -1
        self.current = None
        self.next()
    
    def next(self):
        #TODO: Change implementation when applying multiline support
        self.position += 1
        self.current = self.raw[self.position] if self.position < len(self.raw) else None
    
    def get_tokens(self):
        tokens = []
        while self.current != None:
            if self.current == '+':
                tokens.append(Token(K_ADD,'OPERATOR',self.position))
            elif self.current == '-':
                tokens.append(Token(K_MIN,'OPERATOR',self.position))
            elif self.current == '(':
                tokens.append(Token(K_LPAREN,'OPERATOR',self.position))
            elif self.current == ')':
                tokens.append(Token(K_RPAREN,'OPERATOR',self.position))
            elif self.current == '=':
                tokens.append(Token(K_EQUAL,'OPERATOR',self.position))
            elif self.current == '*':
                tokens.append(Token(K_MUL,'OPERATOR',self.position))
            elif self.current == '/':
                tokens.append(Token(K_DIV,'OPERATOR',self.position))
            elif self.current == ';':
                tokens.append(Token(K_END,'END',self.position))
            elif self.current == ' ':
                pass
            elif self.current in '0123456789':
                num = ''
                decimal_point_count = 0
                while str(self.current) in '.0123456789':
                    if str(self.current) == '.':
                        if decimal_point_count == 1: 
                            return None,error.IllegalSyntax(self.file_name,f"more than 1 decimal point found",self.position,self.line,self.raw)
                        decimal_point_count+=1
                    num += self.current
                    self.next()
                tokens.append(Token(T_NUM,float(num),self.position))
                continue
            elif self.current in string.ascii_letters:
                identifier = ''
                while str(self.current) in string.ascii_letters:
                    identifier += self.current
                    self.next()
                if identifier in K_RESERVED: tokens.append(Token(K_KEYWORD,identifier,self.position))
                else:tokens.append(Token(K_IDENTIFIER,identifier,self.position))
                continue
            else:
                return None,error.UnknownSyntax(self.file_name,f"'{self.current}' is unexpected",self.position,self.line,self.raw)
            self.next()
        tokens.append(Token(S_EOF,'EOF',self.position))
        return tokens,None
