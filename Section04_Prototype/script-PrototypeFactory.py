from Section04_Prototype.PrototypeFactory.EmployeeFactory import EmployeeFactory

# main_office_employee = Employee("", Address("123 East Dr", 0, "London"))
# aux_office_employee = Employee("", Address("123B East Dr", 0, "London"))
# john = copy.deepcopy(main_office_employee)
#john.name = "John"
#john.address.suite = 101
#print(john)
# would prefer to write just one line of code
jane = EmployeeFactory.new_aux_office_employee("Jane", 200)
print(jane)

