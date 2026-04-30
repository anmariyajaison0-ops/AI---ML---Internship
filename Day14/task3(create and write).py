import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    # Header
    writer.writerow(["Name", "Marks"])
    
    # Data
    writer.writerow(["John", 80])
    writer.writerow(["Sara", 90])
    writer.writerow(["Alex", 75])

print("CSV file created successfully!")