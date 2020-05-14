class TrafficAuthority:
    def __init__(self, person):
        self.person = person
        person.property_changed.append(self.person_changed)

    def person_changed(self, name, value):
        if name == 'age':
            if value < 16:
                print('Sorry, you still cannot drive')
            else:
                print('Okay, you can drive now')
                self.person.property_changed.remove(
                    self.person_changed
                )
