class Employee:
    def __init__(self, name, age, position, salary):
        self.__dict__['name'] = name
        self.__dict__['age'] = age
        self.__dict__['position'] = position
        self.__dict__['salary'] = salary

        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(employee, percent):
        employee.salary += employee.salary * (percent/100)

    def employee_info(employee):
        print(f"{employee.name}'s {employee.age} years old. Employee is a {employee.position} with the salary of $ {employee.salary}")

    def print_info(employee):
        print(
            f"{employee.__dict__['name']}'s {employee.__dict__['age']} years old. Employee is a {employee.__dict__['position']} with the salary of $ {employee.__dict__['salary']}")


employee1 = Employee('Vishnu', 25, 'developer', 5000)
employee2 = Employee('Harini', 24, 'tester', 5000)

Employee.print_info(employee1)
Employee.print_info(employee2)

Employee.increase_salary(employee1, 20)

Employee.print_info(employee1)
