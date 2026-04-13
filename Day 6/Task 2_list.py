# ===============================
# TASK 2: LIST PROBLEMS
# ===============================

def list_tasks():

    nums = [10, 20, 5, 40, 15, 20]

    # 1. Find Maximum and Minimum
    print("Max:", max(nums))
    print("Min:", min(nums))


    # 2. Find Second Largest
    unique_nums = list(set(nums))
    unique_nums.sort()
    print("Second Largest:", unique_nums[-2])


    # 3. Remove Duplicates
    print("Without Duplicates:", unique_nums)


    # 4. Count Even and Odd Numbers
    even = 0
    odd = 0

    for n in nums:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Even:", even)
    print("Odd:", odd)

