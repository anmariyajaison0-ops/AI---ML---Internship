# 1. Even numbers
nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)


# 2. Students with marks > 50
marks = [40, 55, 60, 30, 75]
passed = list(filter(lambda x: x > 50, marks))
print(passed)


# 3. Words with length > 5
words = ["python", "ai", "machine", "data"]
long_words = list(filter(lambda x: len(x) > 5, words))
print(long_words)