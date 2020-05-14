from Section23_Visitor.ReflectiveVisitor.AdditionExpression import AdditionExpression
from Section23_Visitor.ReflectiveVisitor.DoubleExpression import DoubleExpression
# still breaks OCP because new types require M×N modifications

if __name__ == '__main__':
    # represents 1+(2+3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    buffer = []
    # ExpressionPrinter.print(e, buffer)
    # IDE might complain here
    e.print(buffer)
    print(''.join(buffer))
