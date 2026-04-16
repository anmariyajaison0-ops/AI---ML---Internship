# Step 1: Read file
students = []

with open("student.txt", "r") as file:
    for line in file:
        name, marks = line.strip().split(",")
        students.append({"name": name, "marks": int(marks)})

# Step 2: Now you can use students

# Filter students > 75
filtered = [s for s in students if s["marks"] > 75]
print(filtered)

# Count students
print("Count:", len(students))

# Lowest marks
low = min(students, key=lambda x: x["marks"])
print("Lowest:", low)

# Sort students
sorted_students = sorted(students, key=lambda x: x["marks"])
print(sorted_students)