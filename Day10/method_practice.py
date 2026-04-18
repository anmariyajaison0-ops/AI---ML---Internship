class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_pass(self):
        return "Pass" if self.marks >= 50 else "Fail"

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "F"

s1 = Student("Anu", 85)
print(s1.is_pass(), s1.grade())