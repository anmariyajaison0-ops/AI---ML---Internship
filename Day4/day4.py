# TASK 2

# Write details
with open("data.txt", "w") as file:
    file.write("Name: Anmariya\nAge: 20\nCourse: AI ML")

# Read file
with open("data.txt", "r") as file:
    print(file.read())

# Append data
with open("data.txt", "a") as file:
    file.write("\nNew Student Added")

# Count lines
with open("data.txt", "r") as file:
    print("Lines:", len(file.readlines()))

# Count words
with open("data.txt", "r") as file:
    print("Words:", len(file.read().split()))

# TASK 3

# Divide by zero + invalid input
try:
    num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print("No error")
finally:
    print("Done")
# TASK 4

# Longest word
with open("data.txt", "r") as file:
    words = file.read().split()
    print("Longest word:", max(words, key=len))

# Count vowels
with open("data.txt", "r") as file:
    text = file.read().lower()
    count = 0
    for ch in text:
        if ch in "aeiou":
            count += 1
    print("Vowels:", count)

# Remove duplicate lines
with open("data.txt", "r") as file:
    lines = file.readlines()

unique_lines = set(lines)

with open("data.txt", "w") as file:
    file.writelines(unique_lines)
