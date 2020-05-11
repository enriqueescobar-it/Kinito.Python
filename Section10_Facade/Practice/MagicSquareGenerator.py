from Section10_Facade.Practice.Generator import Generator
from Section10_Facade.Practice.Splitter import Splitter
from Section10_Facade.Practice.Verifier import Verifier


class MagicSquareGenerator:
    def generate(self, size):
        g = Generator()
        s = Splitter()
        v = Verifier()

        while True:
            square = []
            for x in range(size):
                square.append(g.generate(size))

            if v.verify(s.split(square)):
                break

        return square
