class Number:
    def __init__(self,value):
        self.value = value

    eval = lambda self : int(self.value)

class BinaryOperator:
    def __init__(self,left:Number,right:Number):
        self.left = left
        self.right = right

class Sum(BinaryOperator):
    eval = lambda self : self.left.eval() + self.right.eval()

class Sub(BinaryOperator):
    eval = lambda self : self.left.eval() - self.right.eval()

class Log:
    def __init__(self,value):
        self.value = value
    eval = lambda self : print(self.value.eval())