from Section12_Proxy.ProtectionProxy.CarProxy import CarProxy
from Section12_Proxy.ProtectionProxy.Driver import Driver

if __name__ == '__main__':
    car = CarProxy(Driver('John', 12))
    car.drive()
