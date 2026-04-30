marks = [80, 90]

# Convert to percentage
percentage = [m / 100 for m in marks]

# Multiply values
doubled = [m * 2 for m in marks]

# Normalize (simple scaling 0–1)
normalized = [(m - min(marks)) / (max(marks) - min(marks)) for m in marks]

print(percentage, doubled, normalized)