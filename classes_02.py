class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage/100)


class Tester(Employee):
    def run_tests(self):
        print('Testing is started by {self.name}...')
        print('Tests are done')


class Developer(Employee):
    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percentage, bonus=1000):
        super().increase_salary(percentage)
        # we can also use Employee class to invoke super class method,
        # but this is discouraged since if there is any change in super class name, we have to change this also
        Employee.increase_salary(percentage)
        print('Salary after increament: ', self.salary)
        self.salary += bonus


tester = Tester('Phani', 30, 10000)
# print(tester.salary)
# tester.increase_salary(10)
# print(tester.salary)
# tester.run_tests()


developer = Developer('Vishnu', 25, 10000, 'Flask')
# print(developer.salary)
# developer.increase_salary(10)
# print(developer.salary)


# print('tester is an instance of Tester class? ', isinstance(tester, Tester))
# print('tester is an instance of Employee class? ', isinstance(tester, Employee))

# print('developer is an instance of Tester class? ',
#       isinstance(developer, Tester))
# print('developer is an instance of Developer class? ',
#       isinstance(developer, Developer))
# print('developer is an instance of Employee class? ',
#       isinstance(developer, Employee))

# print('Tester is a sub-class of Employee? ', issubclass(Tester, Employee))
# print('Developer is a sub-class of Employee? ', issubclass(Developer, Employee))
# print('Develoepr is a sub-class of object? ', issubclass(Developer, object))
# print('Employee is a sub-class of object? ', issubclass(Employee, object))

# print(developer.name)
# print(developer.framework)

print(developer.__dict__)
