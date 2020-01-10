import lexer, error, hung_parser


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


class Interpreter:
    def __init__(self, ast, file_name, text, symbol_table):
        self.ast = ast
        self.symbol_table = symbol_table
        self.file_name = file_name
        self.text = text
        self.error = None

    def interpret(self, ast=None):
        ast = ast if ast != None else self.ast
        if isinstance(ast, hung_parser.BinaryOperator):
            number_1 = self.interpret(ast=ast.left)
            number_2 = self.interpret(ast=ast.right)
            if ast.operator.data_type == lexer.K_ADD:
                return number_1 + number_2 if self.error == None else self.error
            if ast.operator.data_type == lexer.K_THEN:
                return number_2 if number_1 == 1.0 else 0.0  if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_MIN:
                return number_1 - number_2 if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_AND:
                return 1.0 if number_2 >= 1.0 and number_1 >= 1.0 else 0.0 if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_OR:
                return 0.0 if number_2 < 1.0 and number_1 < 1.0 else 1.0 if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_MUL:
                return number_1 * number_2 if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_GREATER:
                return 1.0 if number_1 > number_2 else 0.0 if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_SMALLER:
                return 1.0 if number_1 < number_2 else 0.0 if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_COND_EQUAL:
                return 1.0 if number_1 == number_2 else 0.0 if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_DIV:
                if number_2 == 0:
                    self.error = error.RuntimeError(
                        self.file_name, "Division by zero", len(self.text), 1, self.text
                    )
                    return 0 if self.error == None else self.error
                else:
                    return number_1 / number_2 if self.error == None else self.error
        elif isinstance(ast, hung_parser.UnaryOperator):
            number = self.interpret(ast.right)
            if ast.operator.data_type == lexer.K_ADD:
                return number if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_MIN:
                return (number * -1) if self.error == None else self.error
            elif ast.operator.data_type == lexer.K_NOT:
                return 0.0 if number >= 1.0 else 1.0 if self.error == None else self.error
        elif isinstance(ast, hung_parser.Number):
            return ast.token.value if self.error == None else self.error
        elif isinstance(ast, hung_parser.Variable):
            data = self.symbol_table.get_variable(str(ast.token.value))
            if data == None:
                self.error = error.RuntimeError(
                    self.file_name,
                    f'variable "{ast.token.value}" is not defined',
                    ast.token.start + 1,
                    1,
                    self.text,
                )
            return data if self.error == None else self.error
        elif isinstance(ast, hung_parser.CreateVariable):
            data = self.interpret(ast.value)
            self.symbol_table.set_variable(ast.token.value, data)
            return data if self.error == None else self.error
