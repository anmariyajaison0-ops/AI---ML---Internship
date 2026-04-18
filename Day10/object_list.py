class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


students = [
    Student("A", 70),
    Student("B", 95),
    Student("C", 40)
]

# Print all
for s in students:
    print(s.name, s.marks)

# Find topper
topper = max(students, key=lambda x: x.marks)
print("Topper:", topper.name)