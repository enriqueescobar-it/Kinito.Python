from Section10_Facade.RegularFacade.Buffer import Buffer


class Viewport:
    def __init__(self, buffer=Buffer()):
        self.buffer: Buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[self.offset + index]

    def append(self, text):
        self.buffer += text
