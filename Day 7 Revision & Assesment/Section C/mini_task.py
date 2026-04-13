marks = []

for i in range(5):
    m = int(input(f"Enter mark {i+1}: "))
    marks.append(m)

average = sum(marks) / 5
topper = max(marks)

print("Average:", average)
print("Topper mark:", topper)
