import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    
    next(reader)  # Skip header
    
    for row in reader:
        name = row[0]
        marks = row[1]
        print(f"{name} scored {marks} marks")