from Section05_Singleton.SingletonMetaclass.Database import Database

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
