from Section17_Mediator.Practice.Event import Event


class Mediator:
    def __init__(self):
        self.alert = Event()

    def broadcast(self, sender, value):
        self.alert(sender, value)
