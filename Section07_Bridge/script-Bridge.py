# Circles and squares
# Each can be rendered in vector or raster form
from Section07_Bridge.Brigde.Circle import Circle
from Section07_Bridge.Brigde.RasterRenderer import RasterRenderer
from Section07_Bridge.Brigde.VectorRenderer import VectorRenderer

if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
