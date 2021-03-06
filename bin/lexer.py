#####################################################################
# Lexer(Tokenizer) Classes
# Contains all errors that can be raised by the HunG Tokenizer/Lexer.
#####################################################################

# imports
import error
import string

# Tokenizer Constant
T_NUM = "NUM"
T_STR = "STRING"

K_LPAREN = "LPAREN"
K_RPAREN = "RPAREN"
K_END = "END"
K_ADD = "ADD"
K_EQUAL = "EQUAL"
K_MIN = "MIN"
K_MUL = "MUL"
K_THEN = 'THEN'
K_AND = 'AND'
K_OR = 'OR'
K_NOT = "NOT"
K_GREATER = "GREATER"
K_SMALLER = "SMALLER"
K_COND_EQUAL = "COND_EQUAL"
K_DIV = "DIV"
K_IDENTIFIER = "IDENTIFIER"
K_KEYWORD = "KEYWORD"

K_RESERVED = ["var"]

F_LOG = "LOG"

S_EOF = "EOF"


# Token class
class Token:
    def __init__(self, data_type, value, start):
        self.data_type = data_type
        self.start = start
        self.value = value

    def __repr__(self):
        return f"Token({self.data_type},{self.value})"


# Lexer
class Lexer:
    def __init__(self, text: str, file_name):
        self.line = 1  # TODO: FIX MULTILINE SUPPORT
        self.file_name = file_name
        self.raw = text
        self.position = -1
        self.current = None
        self.next()
    #Advance to the next character in the input stream.
    def next(self):
        # TODO: Change implementation when applying multiline support
        self.position += 1
        self.current = (
            self.raw[self.position] if self.position < len(self.raw) else None
        )
    #Get the input stream and generate tokens.
    def get_tokens(self):
        tokens = []
        while self.current != None:
            if self.current == "+":
                tokens.append(Token(K_ADD, "OPERATOR", self.position))
            elif self.current == "-":
                tokens.append(Token(K_MIN, "OPERATOR", self.position))
            elif self.current == "(":
                tokens.append(Token(K_LPAREN, "OPERATOR", self.position))
            elif self.current == "~":
                tokens.append(Token(K_THEN, "OPERATOR", self.position))
            elif self.current == ")":
                tokens.append(Token(K_RPAREN, "OPERATOR", self.position))
            elif self.current == ">":
                tokens.append(Token(K_GREATER, "OPERATOR", self.position))
            elif self.current == "&":
                tokens.append(Token(K_AND, "OPERATOR", self.position))
            elif self.current == "|":
                tokens.append(Token(K_OR, "OPERATOR", self.position))
            elif self.current == "!":
                tokens.append(Token(K_NOT, "OPERATOR", self.position))
            elif self.current == "<":
                tokens.append(Token(K_SMALLER, "OPERATOR", self.position))
            elif self.current == ":":
                tokens.append(Token(K_COND_EQUAL, "OPERATOR", self.position))
            elif self.current == "=":
                tokens.append(Token(K_EQUAL, "OPERATOR", self.position))
            elif self.current == "*":
                tokens.append(Token(K_MUL, "OPERATOR", self.position))
            elif self.current == "/":
                tokens.append(Token(K_DIV, "OPERATOR", self.position))
            elif self.current == ";":
                tokens.append(Token(K_END, "END", self.position))
            elif self.current == " ":
                pass
            elif self.current in "0123456789":
                num = ""
                decimal_point_count = 0
                while str(self.current) in ".0123456789":
                    if str(self.current) == ".":
                        if decimal_point_count == 1:
                            #Raise error for num with more than 1 decimal poins
                            return (
                                None,
                                error.IllegalSyntax(
                                    self.file_name,
                                    f"more than 1 decimal point found",
                                    self.position,
                                    self.line,
                                    self.raw,
                                ),
                            )
                        decimal_point_count += 1
                    num += self.current
                    self.next()
                tokens.append(Token(T_NUM, float(num), self.position))
                continue
            elif self.current in string.ascii_letters:
                #Create identifier
                identifier = ""
                while str(self.current) in string.ascii_letters:
                    identifier += self.current
                    self.next()
                if identifier in K_RESERVED:
                    #If the identifier is inside the reserved keyword then it is a keyword.
                    tokens.append(Token(K_KEYWORD, identifier, self.position))
                else:
                    tokens.append(Token(K_IDENTIFIER, identifier, self.position))
                continue
            else:
                return (
                    None,
                    error.UnknownSyntax(
                        self.file_name,
                        f"'{self.current}' is unexpected",
                        self.position,
                        self.line,
                        self.raw,
                    ),
                )
            self.next()
        tokens.append(Token(S_EOF, "EOF", self.position))
        return tokens, None
