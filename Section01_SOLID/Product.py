from Section01_SOLID.Color import Color
from Section01_SOLID.Size import Size


class Product:
    def __init__(self, name, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size
