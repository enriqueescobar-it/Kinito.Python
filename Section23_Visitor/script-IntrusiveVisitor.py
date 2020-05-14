from Section23_Visitor.IntrusiveVisitor.AdditionExpression import AdditionExpression
from Section23_Visitor.IntrusiveVisitor.DoubleExpression import DoubleExpression

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
    e.print(buffer)
    print(''.join(buffer), '=', e.eval())

    # breaks OCP: requires we modify the entire hierarchy
    # what is more likely: new type or new operation?
