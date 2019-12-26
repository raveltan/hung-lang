import lexer, error

# AST
class Number:
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f"{self.token}"
        #return '(N)'


class BinaryOperator:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"(B|{self.left}, {self.operator}, {self.right})"
        #return f'({self.left},B,{self.right})'


class UnaryOperator:
    def __init__(self, operator, right):
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"(U|{self.operator},{self.right})"
        #return f'(U{self.right})'


# Parser
class Parser:
    def __init__(self, tokens, file_name, text):
        self.tokens = tokens
        self.file_name = file_name
        self.text = text
        self.position = -1
        self.current_token = None
        self.error = None
        self.next()

    def next(self):
        self.position += 1
        self.current_token = (
            self.tokens[self.position] if self.position < len(self.tokens) else None
        )

    def parse(self):
        result = self.level_3()
        return (result,None) if self.error == None else (None,self.error)

    def level_1(self):
        temp_token = self.current_token

        if temp_token.data_type in (lexer.K_MIN, lexer.K_ADD):
            temp_token = self.current_token
            self.next()
            num = self.level_1()
            return UnaryOperator(temp_token,num)
        
        elif temp_token.data_type == lexer.T_NUM:
            self.next()
            if self.current_token.data_type not in (
                lexer.K_MIN,
                lexer.K_ADD,
                lexer.K_MUL,
                lexer.K_DIV,
                lexer.S_EOF,
                lexer.K_LPAREN,
                lexer.K_RPAREN
            ):
                self.error = error.UnknownSyntax(
                    self.file_name,
                    "Expected + , - , * , /",
                    temp_token.start,
                    1,
                    self.text,
                )
            return Number(temp_token)
        
        elif temp_token.data_type == lexer.K_LPAREN:
            self.next()
            expr = self.level_3()
            if self.current_token.data_type == lexer.K_RPAREN:
                self.next
                return expr
            else:
                self.error = error.UnknownSyntax(self.file_name,'Expected ")"',self.position,1,self.text)
        else:
            self.error = error.UnknownSyntax(self.file_name,f'{self.current_token} is unexpected',self.position,1,self.text)

    def level_2(self):
        return self.binary_operator(self.level_1, (lexer.K_MUL, lexer.K_DIV))

    def level_3(self):
        return self.binary_operator(self.level_2, (lexer.K_ADD, lexer.K_MIN))

    def binary_operator(self, function, operator_token):
        left = function()
        while (
            self.current_token.data_type if self.current_token != None else None
        ) in operator_token:
            current_operator_token = self.current_token
            self.next()
            right = function()
            if right == None:
                self.error = error.UnknownSyntax(
                    self.file_name,
                    "Expected NUMBER or EXPRESSION",
                    current_operator_token.start + 1,
                    1,
                    self.text,
                )
            left = BinaryOperator(left, current_operator_token, right)
        if self.current_token.data_type in (lexer.K_LPAREN):
            self.error = error.UnknownSyntax(self.file_name,'Misplacement of "(" or ")"',self.position+1,1,self.text)
        return left


