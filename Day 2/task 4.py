for i in range(1, 21):
    print(i)
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
n = int(input("Enter N: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum:", sum)
for i in range(10, 0, -1):
    print(i)