from Section19_Observer.DependenciesObserver.Person import Person

if __name__ == '__main__':
    def person_changed(name, value):
        if name == 'can_vote':
            print(f'Voting status changed to {value}')


    p = Person()
    p.property_changed.append(
        person_changed
    )

    for age in range(16, 21):
        print(f'Changing age to {age}')
        p.age = age
