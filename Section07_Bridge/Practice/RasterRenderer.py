from Section07_Bridge.Practice.Renderer import Renderer


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'pixels'
