from Section23_Visitor.ReflectiveVisitor.AbstractExpression import AbstractExpression


class AdditionExpression(AbstractExpression):
    def __init__(self, left, right):
        self.right = right
        self.left = left
