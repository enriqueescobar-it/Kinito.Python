class ChatRoom:
    def __init__(self):
        self.people = []

    def broadcast(self, source, message):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    def join(self, person):
        join_msg = f'{person.name} joins the chat'
        self.broadcast('room', join_msg)
        person.room = self
        self.people.append(person)

    def message(self, source, destination, message):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)
