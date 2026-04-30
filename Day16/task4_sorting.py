students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": None},
    {"name": "C", "marks": 40},
    {"name": "D", "marks": -10}
]

# Clean data first
cleaned = [s for s in students if s["marks"] is not None and s["marks"] >= 0]
cleaned.sort(key=lambda x: x["marks"], reverse=True)

print("Sorted students:")
print(cleaned)
top3 = cleaned[:3]

print("Top 3 students:")
print(top3)