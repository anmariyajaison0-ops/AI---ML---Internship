# 1. Number generator
def gen(n):
    for i in range(n):
        yield i

# 2. Even numbers generator
def even_gen(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

# 3. Fibonacci generator
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
print(list(gen(5)))
print(list(even_gen(10)))
print(list(fib(7)))