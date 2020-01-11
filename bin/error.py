#####################################################################
# Error Classes
# Contains all errors that can be raised by the HunG Interpreter
#####################################################################
class Error:
    #The Error class the all errors with inherit.
    def __init__(self, name, file_name, desc, cursor, line, text: str):
        self.name = name
        self.desc = desc
        self.file_name = file_name
        self.cursor = cursor
        self.line = line
        self.text: str = text

    def __repr__(self):
        error = (
            f"\n<{self.file_name}:{self.line}:{self.cursor}> {self.name}, {self.desc}"
        )
        detail = f"\n{self.text}\n" + " " * self.cursor + "^"
        return str(error + detail)


class IllegalSyntax(Error):
    #Illegal Syntax Error, will be raised by the LEXER when user type an unknown syntax.
    def __init__(self, file_name, desc, cursor, line, text):
        super().__init__("Illegal Syntax", file_name, desc, cursor, line, text)


class UnknownSyntax(Error):
    #Unknown Syntax Error, will be raised by the PARSER when certain token(s) is unintelligable.
    def __init__(self, file_name, desc, cursor, line, text):
        super().__init__("Unknown Syntax", file_name, desc, cursor, line, text)


class RuntimeError(Error):
    #Runtime Error, will be raised by the INTERPRETER when certain AST(s) are running invalid syntax.
    def __init__(self, file_name, desc, cursor, line, text):
        super().__init__("Runtime Error", file_name, desc, cursor, line, text)

