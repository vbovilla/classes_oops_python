class Employee:
    def __init__(self):
        self.__dict__['name'] = 'Vishnu'
        self.__dict__['age'] = 25
        self.__dict__['position'] = 'developer'
        self.__dict__['salary'] = 5000
        self.name = 'Vishnu'
        self.age = 25
        self.position = 'developer'
        self.salary = 5000


e = Employee()  # this calls 2 functions: __new__ and __init__
# __new__ : allocates memory for a new object and send it to the __init__ function
# __init__ : receive a new object from the __new__ function as a 'self' parameter

print(e)
print(e.__dict__)
print(e.__class__)
