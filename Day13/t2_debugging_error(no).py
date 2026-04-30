#Before
#nums = [1, 2, 3]
print(nums[5])
#After
nums = [1, 2, 3]

if len(nums) > 5:
    print(nums[5])
else:
    print("Index out of range")