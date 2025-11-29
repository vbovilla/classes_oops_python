class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increment_salary(self, percentage):
        self.salary += self.salary * (percentage/100)

    def print_info(self):
        print(f"{self.name}'s {self.age} years old. Employee is a {self.position} with the salary of $ {self.salary}")

    def __str__(self):
        return f"{self.name}'s {self.age} years old. Employee is a {self.position} with the salary of $ {self.salary}"

    def __repr__(self):
        return f"Employee({repr(self.name)}, {repr(self.age)}, {repr(self.position)}, {repr(self.salary)})"


employee1 = Employee('Vishnu', 25, 'developer', 5000)
employee2 = Employee('Harini', 24, 'tester', 5000)

# employee1.print_info()
print(employee1)
print(employee2)

# str is a global method, which will invoke the overidden __str__ in this class
print(str(employee1))
print(str(employee2))

print(repr(employee1))
print(repr(employee2))

print(eval(repr(employee1)))
print(eval(repr(employee2)))


# Dunder methods
# Special "magic" methods that start and end with the double underscore. Usually, invoked by a special syntax
