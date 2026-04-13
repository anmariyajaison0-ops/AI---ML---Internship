# ===============================
# TASK 7: LOGIC CHALLENGES
# ===============================

def logic_tasks():

    nums = [10, 20, 5, 40, 15, 20]

    # 1. Find Second Smallest Number
    unique_nums = list(set(nums))
    unique_nums.sort()
    print("Second Smallest:", unique_nums[1])


    # 2. Merge Two Lists Without Duplicates
    a = [1, 2, 3]
    b = [3, 4, 5]

    merged = list(set(a + b))
    print("Merged List:", merged)


    # 3. Find Frequency of Elements
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    print("Frequency:", freq)