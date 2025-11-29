class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self._annual_salary = None
        self._employee_id = None  # can not set None also as it is a read-only property

    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage/100)

    def __str__(self):
        return f"{self.name}'s is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}"

    def __repr__(self):
        return (
            f"Employee({repr(self.name)}, {repr(self.age)}, {repr(self.position)}, {repr(self.salary)})"
        )

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._annual_salary = None
        if salary < 1000:
            raise ValueError('Minimum wage is $1000')
        else:
            self._salary = salary

    @property
    def employee_id(self):
        return '10001'

    @employee_id.setter
    def employee_id(self, employee_id):
        raise AttributeError('Employee Id is read-only')
        # self.employee_id = employee_id

    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self.salary*12
        return self._annual_salary


employee1 = Employee('Vishnu', 25, 'developer', 5000)
employee2 = Employee('Harini', 24, 'tester', 5000)

# employee1.salary = 10000
# print('employee1 salary', employee1.salary)

# print('employee1 id: ', employee1.employee_id)
# employee1.employee_id = 1001

print('employee1 annual salaary: ', employee1.annual_salary)

employee1.increase_salary(20)

print('employee1 annual salaary: ', employee1.annual_salary)
print('employee2 annual salaary: ', employee2.annual_salary)
