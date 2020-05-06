import copy

from Section04_Prototype.PrototypeFactory.Address import Address
from Section04_Prototype.PrototypeFactory.Employee import Employee


class EmployeeFactory:
    main_office_employee: Employee = Employee("", Address("123 East Dr", 0, "London"))
    aux_office_employee: Employee = Employee("", Address("123B East Dr", 0, "London"))

    @staticmethod
    def __new_employee(proto, name, suite) -> Employee:
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name, suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name, suite
        )
