TT_NUM = 'NUM'
TT_FLOAT = 'FLOAT'
TT_ADD = 'ADD'
TT_SUB = 'SUB'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_OPEN_PAREN = 'OPEN_PAREN'
TT_CLOSE_PAREN = 'CLOSE_PAREN'

class Token:
    def __init__(self,data_type,value=None):
        self.type = data_type
        self.value = value
    def __repr__(self):
        return f'Token({self.type},{self.value})' if self.value else f'Token({self.type})'