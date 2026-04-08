students = [
    {"name": "A", "marks": 70},
    {"name": "B", "marks": 85},
    {"name": "C", "marks": 90},
    {"name": "D", "marks": 60},
    {"name": "E", "marks": 78}
]

# Print all students
for s in students:
    print(s)

# Average marks
total = sum(s["marks"] for s in students)
print("Average:", total / len(students))

# Highest marks
print("Highest:", max(s["marks"] for s in students))

# Students with marks > 75
for s in students:
    if s["marks"] > 75:
        print(s["name"])