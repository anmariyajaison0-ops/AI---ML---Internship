num = int(input("Enter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
marks = int(input("Enter marks: "))

if marks > 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")