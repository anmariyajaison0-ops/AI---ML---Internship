# 1. Remove duplicates
nums = [1, 2, 2, 3]
unique = set(nums)

# 2. Common elements
a = {1, 2, 3}
b = {2, 3, 4}
common = a & b

# 3. Union and difference
union = a | b
diff = a - b
print(unique)
print(common)
print(union)
print(diff)