# employee1 = ['Vishnu', 25, 'developer', 5000]
# employee2 = ['Harini', 24, 'tester', 5000]

# employees = [employee1, employee2]
# for e in employees:
#     print(f"{e[0]}'s salary is ${e[3]}")


employee1 = {
    "name": "Vishnu",
    "age": 25,
    'position': 'developer',
    'salary': 5000
}

employee2 = {
    "name": "Harini",
    "age": 25,
    'position': 'tester',
    'salary': 5000
}


def init_employee(name, age, position, salary):
    return {
        'name': name,
        'age': age,
        'position': position,
        'salary': salary
    }


employee3 = init_employee('Vishnu', 38, 'developer', 5000)

employees = [employee1, employee2, employee3]

for e in employees:
    # print(f"{e[0]}'s salary is ${e[3]}") # will not work incase of dictionaries
    print(f"{e['name']}'s salary is $ {e['salary']}")


def increase_salary(employee, percent):
    employee['salary'] += employee['salary']*(percent/100)


def employee_info(employee):
    print(f"{employee['name']} is {employee['age']} years old. Employee is a {employee['position']} with the salary of $ {employee['salary']}")


increase_salary(employee2, 20)

for e in employees:
    employee_info(e)
