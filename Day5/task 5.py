# Second highest number
nums = [10, 20, 30, 40]
nums = list(set(nums))
nums.sort()
print(nums[-2])

# Count frequency of characters
text = "python"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

# Remove duplicates
nums = [1, 2, 2, 3, 4, 4]
print(list(set(nums)))