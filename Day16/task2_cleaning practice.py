students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": None},
    {"name": "C", "marks": 40},
    {"name": "D", "marks": -10}
]

# Keep only valid data
cleaned = [s for s in students if s["marks"] is not None and s["marks"] >= 0]

print(cleaned)