from Section02_Builder.BuilderInheritance.PersonBirthDateBuilder import PersonBirthDateBuilder

if __name__ == '__main__':
    pb = PersonBirthDateBuilder()
    me = pb\
        .called('Dmitri')\
        .works_as_a('quant')\
        .born('1/1/1980')\
        .build()  # this does NOT work in C#/C++/Java/...
    print(me)
