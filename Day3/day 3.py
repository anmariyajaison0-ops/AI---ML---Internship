# TASK: Sum of list
nums = [1,2,3,4,5]
print(sum(nums))

# TASK: Max number
print(max(nums))

# TASK: Even numbers
for i in nums:
    if i % 2 == 0:
        print(i)
#------Task 2-------
# Create list
nums = [1,2,3,4,5,6,7,8,9,10]

# Sum
print("Sum:", sum(nums))

# Max
print("Max:", max(nums))

# Even numbers
print("Even numbers:")
for i in nums:
    if i % 2 == 0:
        print(i)

# Reverse
print("Reverse:", nums[::-1])
#------Task 3-------
student = {
    "name": "Anu",
    "age": 20,
    "marks": 85
}

# Update marks
student["marks"] = 90

# Add grade
student["grade"] = "A"

# Print
print(student)
#------Task 4-------
text = "madam"

# Length
print("Length:", len(text))

# Reverse
print("Reverse:", text[::-1])

# Palindrome
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Vowels count
vowels = "aeiou"
count = 0
for ch in text:
    if ch in vowels:
        count += 1

print("Vowels:", count)
#------Task 5-------
# Remove duplicates
lst = [1,2,2,3,4,4,5]
print(set(lst))

# Common elements
a = {1,2,3}
b = {2,3,4}
print(a & b)
#------Task 6-------
# Squares
squares = [x*x for x in range(1,11)]
print(squares)

# Even numbers
evens = [x for x in range(1,21) if x % 2 == 0]
print(evens)
