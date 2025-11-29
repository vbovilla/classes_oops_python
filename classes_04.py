from datetime import date


class Employee:
    minimum_wage = 1000  # class attributes

    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    # class level functions which do not need objects to be invoked. these are similar to static methods in Java.
    @classmethod
    def change_minimum_wage(cls, minimum_wage):
        if minimum_wage > 3000:
            raise ValueError('Company will bankrupt')
        elif minimum_wage < Employee.minimum_wage:
            raise ValueError('Employee can not survive')
        else:
            Employee.minimum_wage = minimum_wage

    @classmethod    # factory functions
    def new_employee(cls, name, dob):
        now = date.today()
        age = now.year - dob.year - \
            ((now.month, now.daya) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)

    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage/100)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < Employee.minimum_wage:
            raise ValueError(f'Minimum wage is $ {Employee.minimum_wage}')
        else:
            self._salary = salary


print(Employee.__dict__)

e = Employee('Vishnu', 25, 'developer', 10000)
print(e.salary)
Employee.__dict__['increase_salary'](e, 10)
print(e.salary)


print(e.minimum_wage)
print(Employee.minimum_wage)


# change minimum wage
Employee.change_minimum_wage(2000)

# e.salary = 1500
# print(e.salary)

print(Employee.minimum_wage)
