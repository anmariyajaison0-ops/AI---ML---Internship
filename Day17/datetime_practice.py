import datetime

now = datetime.datetime.now()

# Current date
print(now)

# Formatted date
print(now.strftime("%Y-%m-%d"))

# Extract year and month
print(now.year)
print(now.month)