from Section02_Builder.PersonBuilder import PersonBuilder

if __name__ == '__main__':
    pb = PersonBuilder()
    p = pb\
        .lives\
            .at('123 London Road')\
            .in_city('London')\
            .with_postcode('SW12BC')\
        .works\
            .at('Fabrikam')\
            .as_a('Engineer')\
            .earning(123000)\
        .build()
    print(p)
    person2 = PersonBuilder().build()
    print(person2)
