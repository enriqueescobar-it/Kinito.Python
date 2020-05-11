from Section08_Composite.NeuralNetworks.Connectable import Connectable


class Neuron(Connectable):
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    # def connect_to(self, other):
    #     self.outputs.append(other)
    #     other.inputs.append(self)

    def __iter__(self):
        yield self

    def __str__(self):
        return f'{self.name}, {len(self.inputs)} inputs, {len(self.outputs)} outputs'
