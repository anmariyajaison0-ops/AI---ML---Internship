nums = [1, 2, 3, 4]

# 1. Number-square dict
sq_dict = {x: x*x for x in nums}

# 2. Even numbers
even_dict = {x: x*x for x in nums if x % 2 == 0}

# 3. Name length mapping
names = ["AI", "Python"]
length_dict = {n: len(n) for n in names}
print(sq_dict)
print(even_dict)
print(length_dict)