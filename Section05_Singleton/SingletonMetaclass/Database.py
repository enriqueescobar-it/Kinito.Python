from Section05_Singleton.SingletonMetaclass.Singleton import Singleton


class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading database')
