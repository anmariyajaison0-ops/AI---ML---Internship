import csv
import json

data = []

# Read CSV
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        row["Marks"] = int(row["Marks"])  # convert to number
        data.append(row)

# Write JSON
with open("students.json", "w") as file:
    json.dump(data, file, indent=4)

print("Task 4 completed!")