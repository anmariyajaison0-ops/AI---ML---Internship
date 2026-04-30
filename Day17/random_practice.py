import random

# Random number
print(random.randint(1, 100))

# Random element
print(random.choice([5, 10, 15, 20]))

# List of random numbers
numbers = [random.randint(1, 50) for i in range(5)]
print(numbers)