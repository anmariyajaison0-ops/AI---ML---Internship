import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [50, 70, 90]

# Line graph
plt.figure()
plt.plot(x, y)
plt.title("Line Graph")
plt.show()

# Bar chart
plt.figure()
plt.bar(x, y)
plt.title("Bar Chart")
plt.show()
