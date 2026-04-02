#scatter plot
#Enrollment Number : 92400527159 Name : Przthzm Nichani

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 15, 7, 25, 30, 10, 20, 35]
sizes = [20, 40, 60, 80, 100, 120, 140, 160]
colors = ['red', 'blue', 'green', 'purple', 'orange', 'pink', 'black', 'brown']

# Creating scatter plot with custom colors and sizes
plt.scatter(x, y, s=sizes, c=colors, marker="o")

# Adding labels and title
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot with Colors and Sizes")

# Show plot
plt.show()
