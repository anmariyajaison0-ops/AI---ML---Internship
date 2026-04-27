class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


e = Employee("Anu", 40000)
e.display_details()