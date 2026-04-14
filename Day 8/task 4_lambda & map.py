# 1. Square all numbers
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print(squares)


# 2. Double values
double = list(map(lambda x: x*2, nums))
print(double)


# 3. Convert to uppercase
words = ["ai", "ml", "python"]
upper = list(map(lambda x: x.upper(), words))
print(upper)