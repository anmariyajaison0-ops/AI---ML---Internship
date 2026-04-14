# 1. Factorial using recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))


# 2. Sum of numbers using recursion
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n-1)

print(sum_numbers(5))


# 3. Fibonacci series
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(6):
    print(fibonacci(i), end=" ")