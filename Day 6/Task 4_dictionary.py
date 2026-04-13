# ===============================
# TASK 4: DICTIONARY PROBLEMS
# ===============================

def dictionary_tasks():

    # 1. Create Student List
    students = [
        {"name": "A", "marks": 70},
        {"name": "B", "marks": 90},
        {"name": "C", "marks": 60}
    ]


    # 2. Find Topper
    top = students[0]
    for s in students:
        if s["marks"] > top["marks"]:
            top = s

    print("Topper:", top)


    # 3. Calculate Average
    total = 0
    for s in students:
        total += s["marks"]

    avg = total / len(students)
    print("Average:", avg)


    # 4. Filter Passed Students
    passed = []
    for s in students:
        if s["marks"] >= 50:
            passed.append(s)

    print("Passed:", passed)