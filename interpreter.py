from parser import Number,BinaryOperator,UnaryOperator,Parser
import lexer,error

class Interpreter:
    def __init__(self,ast,file_name,text):
        self.ast = ast
        self.file_name = file_name
        self.text = text
        self.error = None
    def interpret(self,ast=None):
        ast = ast if ast != None else self.ast
        if isinstance(ast,BinaryOperator):
            number_1 = self.interpret(ast=ast.left)
            number_2 = self.interpret(ast=ast.right)
            if ast.operator.data_type == lexer.K_ADD:
                return number_1 + number_2 if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_MIN:
                return number_1 - number_2 if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_MUL:
                return number_1 * number_2 if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_DIV:
                if number_2 == 0:
                    self.error =error.RunTimeError(self.file_name,'Division by zero',len(self.text),1,self.text)
                    return 0 if self.error == None else self.error
                else:
                    return number_1*number_2 if self.error == None else self.error
        elif isinstance(ast,UnaryOperator):
            number = self.interpret(ast.right)
            if ast.operator.data_type == lexer.K_ADD:
                return +number if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_MIN:
                return -number if self.error == None else self.error
        elif isinstance(ast,Number):
            return ast.token.value if self.error == None else self.error
