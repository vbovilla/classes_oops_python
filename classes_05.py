from dataclasses import dataclass


# class Project:
#     def __init__(self, name, payment, client):
#         self.name = name
#         self.payment = payment
#         self.client = client

#     def __repr__(self):
#         return f"Project(name={repr(self.name)}, payment={repr(self.payment)}, client={repr(self.client)})"

@dataclass
class Project:
    name: str
    payment: str
    client: str


class Employee:
    def __init__(self, name, age, position, salary, project):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.project = project


p = Project('Django application', 200000, 'Globomantics')
e = Employee('Vishnu', 25, 'developer', 1000, p)

print(e.project)
