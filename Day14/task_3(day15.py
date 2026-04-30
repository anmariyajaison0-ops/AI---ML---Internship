marks = [80, -10, None, 90, 70, -5]

cleaned = [m for m in marks if m is not None and m >= 0]

print(cleaned)