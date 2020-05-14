from Section23_Visitor.ReflectiveVisitor.AbstractExpression import AbstractExpression


class DoubleExpression(AbstractExpression):
    def __init__(self, value):
        self.value = value
