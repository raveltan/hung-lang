#####################################################################
# Interpreter-related Classes
# Contains all classes that is directly corelated to the work of the Interpreter.
#####################################################################


import lexer, error, hung_parser

#The class that is responsible for storing and accessing variable.
class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.parent = None

    def get_variable(self, name):
        return self.symbols.get(name, None)

    def set_variable(self, name, data):
        self.symbols[name] = data

    def remove(self, name):
        del self.symbols[name]

    def dump(self):
        return self.symbols

#The Interpreter of HunG programming language.
class Interpreter:
    def __init__(self, ast, file_name, text, symbol_table):
        self.ast = ast
        self.symbol_table = symbol_table
        self.file_name = file_name
        self.text = text
        self.error = None
    #interpret function to convert the AST from the parser to a result.
    def interpret(self, ast=None):
        ast = ast if ast != None else self.ast
        #check if the current AST is a Binary Operation
        if isinstance(ast, hung_parser.BinaryOperator):
            number_1 = self.interpret(ast=ast.left)
            number_2 = self.interpret(ast=ast.right)
            if ast.operator.data_type == lexer.K_ADD: #Addition
                return number_1 + number_2 if self.error == None else self.error
            if ast.operator.data_type == lexer.K_THEN: #If statement
                return number_2 if number_1 == 1.0 else 0.0  if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_MIN: #Substraction
                return number_1 - number_2 if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_AND: #Bitwise AND
                return 1.0 if number_2 >= 1.0 and number_1 >= 1.0 else 0.0 if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_OR: #Bitwise OR
                return 0.0 if number_2 < 1.0 and number_1 < 1.0 else 1.0 if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_MUL: #Multiplication
                return number_1 * number_2 if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_GREATER: #Comparator Greater
                return 1.0 if number_1 > number_2 else 0.0 if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_SMALLER: #Comparator Smaller
                return 1.0 if number_1 < number_2 else 0.0 if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_COND_EQUAL: #Comparator Equal
                return 1.0 if number_1 == number_2 else 0.0 if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_DIV: #Division
                if number_2 == 0:
                    #Raise an Error in case of division by zero.
                    self.error = error.RuntimeError(
                        self.file_name, "Division by zero", len(self.text), 1, self.text
                    )
                    return 0 if self.error == None else self.error
                else:
                    return number_1 / number_2 if self.error == None else self.error
        #Check if the current AST is an Unary Operation
        elif isinstance(ast, hung_parser.UnaryOperator):
            number = self.interpret(ast.right)
            if ast.operator.data_type == lexer.K_ADD: #PLUS
                return number if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_MIN: #MIN
                return (number * -1) if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_NOT: #NOT
                return 0.0 if number >= 1.0 else 1.0 if self.error == None else self.error
        #Return number value for number AST
        elif isinstance(ast, hung_parser.Number):
            return ast.token.value if self.error == None else self.error
        #Check if current AST is a Variable access AST
        elif isinstance(ast, hung_parser.Variable):
            data = self.symbol_table.get_variable(str(ast.token.value))
            if data == None:
                #Raise an Error when certain variable is not yet initialized.
                self.error = error.RuntimeError(
                    self.file_name,
                    f'variable "{ast.token.value}" is not defined',
                    ast.token.start + 1,
                    1,
                    self.text,
                )
            return data if self.error == None else self.error
        #Check if current AST is a Create Variable AST
        elif isinstance(ast, hung_parser.CreateVariable):
            data = self.interpret(ast.value)
            #Add current variable to the symbol table.
            self.symbol_table.set_variable(ast.token.value, data)
            return data if self.error == None else self.error
