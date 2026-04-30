students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": None},
    {"name": "C", "marks": 40},
    {"name": "D", "marks": -10}
]

# Create cleaned data first
cleaned = [s for s in students if s["marks"] is not None and s["marks"] >= 0]

# Now transformation works
for s in cleaned:
    s["status"] = "Pass" if s["marks"] >= 50 else "Fail"
    s["percentage"] = s["marks"]

    if s["marks"] >= 75:
        s["grade"] = "A"
    elif s["marks"] >= 50:
        s["grade"] = "B"
    else:
        s["grade"] = "C"

print(cleaned)