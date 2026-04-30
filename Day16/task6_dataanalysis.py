students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": None},
    {"name": "C", "marks": 40},
    {"name": "D", "marks": -10}
]

cleaned = [s for s in students if s["marks"] is not None and s["marks"] >= 0]
marks = [s["marks"] for s in cleaned]
average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)