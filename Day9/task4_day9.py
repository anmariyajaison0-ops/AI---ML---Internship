# Step 1: Read file and create students list
students = []

with open("student.txt", "r") as file:
    for line in file:
        name, marks = line.strip().split(",")
        students.append({"name": name, "marks": int(marks)})

# Step 2: Define functions
def get_average(students):
    return sum(s["marks"] for s in students) / len(students)

def get_topper(students):
    return max(students, key=lambda x: x["marks"])

def filter_students(students):
    return [s for s in students if s["marks"] > 75]

# Step 3: Call functions
print(get_average(students))
print(get_topper(students))
print(filter_students(students))