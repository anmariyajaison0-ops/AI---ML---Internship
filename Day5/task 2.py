# Reverse a string
text = "python"
print(text[::-1])

# Count number of words
text = "AI ML Python"
print(len(text.split()))

# Check palindrome
text = "madam"
print(text == text[::-1])

# Replace words
text = "hello ai"
print(text.replace("ai", "ml"))

# Count vowels
text = "machine learning"
vowels = "aeiou"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print(count)
