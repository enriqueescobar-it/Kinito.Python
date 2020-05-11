from Section07_Bridge.Brigde.Renderer import Renderer


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for circle of radius {radius}')
