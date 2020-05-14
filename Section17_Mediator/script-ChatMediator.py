from Section17_Mediator.ChatMediator.ChatRoom import ChatRoom
from Section17_Mediator.ChatMediator.Person import Person

if __name__ == '__main__':
    room = ChatRoom()
    john = Person('John')
    jane = Person('Jane')
    room.join(john)
    room.join(jane)
    john.say('hi room')
    jane.say('oh, hey john')
    simon = Person('Simon')
    room.join(simon)
    simon.say('hi everyone!')
    jane.private_message('Simon', 'glad you could join us!')
