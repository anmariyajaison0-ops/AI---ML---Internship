marks = [80, 40, 90, 30, 76, 88]

# Passed students
passed = [m for m in marks if m >= 50]

# Marks > 75
above_75 = [m for m in marks if m > 75]

# Even numbers
even = [m for m in marks if m % 2 == 0]

print(passed, above_75, even)