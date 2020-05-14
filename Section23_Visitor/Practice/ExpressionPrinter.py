from Section23_Visitor.Practice.AdditionExpression import AdditionExpression
from Section23_Visitor.Practice.MultiplicationExpression import MultiplicationExpression
from Section23_Visitor.Practice.Value import Value


class ExpressionPrinter:
    def __init__(self):
        self.buffer = []

    @visitor(Value)
    def visit(self, e):
        self.buffer.append(str(e.value))

    @visitor(AdditionExpression)
    def visit(self, e):
        self.buffer.append('(')
        self.visit(e.left)
        self.buffer.append('+')
        self.visit(e.right)
        self.buffer.append(')')

    @visitor(MultiplicationExpression)
    def visit(self, e):
        self.visit(e.left)
        self.buffer.append('*')
        self.visit(e.right)

    def __str__(self):
        return ''.join(self.buffer)
