#Shivansh's Python Code (E22CSEU1004)

class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"

    def __lt__(self, other):
        if sort_by == 1:
            return self.age < other.age
        elif sort_by == 2:
            return self.name < other.name
        else:
            return self.salary < other.salary

employees = [
    Employee("161E90", "Raman", 41, 56000),
    Employee("161F91", "Himadri", 38, 67500),
    Employee("161F99", "Jaya", 51, 82100),
    Employee("171E20", "Tejas", 30, 55000),
    Employee("171G30", "Ajay", 45, 44000)
]

sort_by = int(input("Enter sorting parameter (1. Age, 2. Name, 3. Salary): "))
employees.sort()

for employee in employees:
    print(employee)
