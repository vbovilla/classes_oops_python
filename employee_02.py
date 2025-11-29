class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary


e1 = Employee('Vishnu', 25, 'developer', 5000)
e2 = Employee('Harini', 24, 'tester', 5000)

print(e1)
print(e1.name)
print(e1.__dict__)
print(e1.__class__)
print('\n\n')
print(e2)
print(e2.__dict__)
print(e2.__class__)
print(e2.name)
