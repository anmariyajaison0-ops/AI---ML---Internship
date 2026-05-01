# 1. Combine lists
names = ["A", "B"]
marks = [80, 90]
combined = list(zip(names, marks))

# 2. Print index + value
for i, v in enumerate(names):
    print(i, v)

# 3. Zip to dictionary
d = dict(zip(names, marks))
print(combined)
print(d)