students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": None},
    {"name": "C", "marks": 40},
    {"name": "D", "marks": -10}
]

cleaned = [s for s in students if s["marks"] is not None and s["marks"] >= 0]
result = {"pass": [], "fail": []}

for s in cleaned:
    if s["marks"] >= 50:
        result["pass"].append(s)
    else:
        result["fail"].append(s)

print(result)
print("Pass count:", len(result["pass"]))
print("Fail count:", len(result["fail"]))