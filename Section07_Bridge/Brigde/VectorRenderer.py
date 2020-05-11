from Section07_Bridge.Brigde.Renderer import Renderer


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')
