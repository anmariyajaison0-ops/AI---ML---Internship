nums = [10, 20, 30, 60, 80]

# 1. Square numbers
squares = [x*x for x in nums]

# 2. Even numbers
even = [x for x in nums if x % 2 == 0]

# 3. Uppercase
names = ["ai", "ml"]
upper = [n.upper() for n in names]

# 4. Numbers > 50
gt50 = [x for x in nums if x > 50]
print(squares)
print(even)
print(upper)
print(gt50)