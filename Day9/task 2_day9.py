# Step 1: Read file
students = []

with open("student.txt", "r") as file:
    for line in file:
        name, marks = line.strip().split(",")
        students.append({"name": name, "marks": int(marks)})

# Step 2: Print all students
print(students)

# Step 3: Average marks
total = sum(s["marks"] for s in students)
avg = total / len(students)
print("Average:", avg)

# Step 4: Topper
top = max(students, key=lambda x: x["marks"])
print("Topper:", top["name"])