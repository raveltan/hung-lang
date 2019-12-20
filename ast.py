from rply.token import BaseBox

class Number(BaseBox):
    def __init__(self, value):
        self.value = value
    def eval(self):
        return self.value

class BinaryOperator(BaseBox):
    def __init__(self,left,right):
        self.left = left
        self.right = right

class Add(BinaryOperator):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOperator):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mul(BinaryOperator):
    def eval(self):
        return self.left.eval() * self.right.eval()

class Div(BinaryOperator):
    def eval(self):
        return self.left.eval() / self.right.eval()
