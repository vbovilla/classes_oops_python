class SlotsInspectorMixin:
    __slots__ = ()

    def has_slots(self):
        return hasattr(self, '__slots__')


class Employee:
    __slots__ = ('name', 'age', 'position', 'salary')

    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage/100)

    def has_slots(self):
        return hasattr(self, '__slots__')


class Tester(Employee):
    def run_tests(self):
        print('Testing is started by {self.name}...')
        print('Tests are done')


class Developer(Employee, SlotsInspectorMixin):
    __slots__ = ('framework')

    def __init__(self, name, age, position, salary, framework):
        super().__init__(name, age, position, salary)
        self.framework = framework

    def increase_salary(self, percentage, bonus):
        super().increase_salary(percentage)
        self.salary += bonus


developer = Developer('Vishnu', 25, 'developer', 1000, 'Flask')
print('has slots? ', developer.has_slots())
print('method ordering: ', Developer.__mro__)
# print(Developer.__slots__)
print(Developer.__dict__)

# tester = Tester('Phani', 30, 'tester', 10000)
# print(tester)
