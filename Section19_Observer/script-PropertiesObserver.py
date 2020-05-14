from Section19_Observer.PropertiesObserver.Person import Person
from Section19_Observer.PropertiesObserver.TrafficAuthority import TrafficAuthority

if __name__ == '__main__':
    p = Person()
    ta = TrafficAuthority(p)
    for age in range(14, 20):
        print(f'Setting age to {age}')
        p.age = age
