# 1. Sum of digits using recursion
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))


# 2. Flatten nested list
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

print(flatten([1, [2, 3], [4, [5]]]))


# 3. Count occurrences using dictionary
def count_occurrences(lst):
    freq = {}
    for i in lst:
        freq[i] = freq.get(i, 0) + 1
    return freq

print(count_occurrences([1, 2, 2, 3, 3, 3]))