from Section10_Facade.RegularFacade.Buffer import Buffer
from Section10_Facade.RegularFacade.Viewport import Viewport


class Console:
    def __init__(self):
        b = Buffer()
        self.current_viewport: Viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    # high-level
    def write(self, text):
        self.current_viewport.buffer.write(text)

    # low-level
    def get_char_at(self, index):
        return self.current_viewport.get_char_at(index)
