#Before
nums = [1, 2, 3]

total = 0
for i in nums:
    total += i
print(total)

total = 0
for i in nums:
    total += i
print(total)
#After
def get_sum(numbers):
    return sum(numbers)

nums = [1, 2, 3]

print(get_sum(nums))
print(get_sum(nums))