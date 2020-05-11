from Section07_Bridge.Practice.Renderer import Renderer


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'lines'
