from Section08_Composite.GeometricShapes.Circle import Circle
from Section08_Composite.GeometricShapes.GraphicObject import GraphicObject
from Section08_Composite.GeometricShapes.Square import Square

if __name__ == '__main__':
    drawing = GraphicObject()
    drawing._name = 'My Drawing'
    drawing.children.append(Square('Red'))
    drawing.children.append(Circle('Yellow'))

    group = GraphicObject()  # no name
    group.children.append(Circle('Blue'))
    group.children.append(Square('Blue'))
    drawing.children.append(group)

    print(drawing)
