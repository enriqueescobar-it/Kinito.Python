from Section19_Observer.EventsObserver.Person import Person


def call_doctor(name, address):
    print(f'A doctor has been called to {address}')


if __name__ == '__main__':
    person = Person('Sherlock', '221B Baker St')
    person.falls_ill.append(lambda name, addr: print(f'{name} is ill'))
    person.falls_ill.append(call_doctor)
    person.catch_a_cold()
    # and you can remove subscriptions too
    person.falls_ill.remove(call_doctor)
    person.catch_a_cold()
