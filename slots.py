class Developer:
    __slots__ = ('name', 'age', 'position', 'salary', 'framework')

    def __init__(self, name, age, position, salary, framework):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.framework = framework


developer = Developer('Vishnu', 25, 'developer', 5000, 'Flask')

print(developer.__slots__)
print(developer.framework)
