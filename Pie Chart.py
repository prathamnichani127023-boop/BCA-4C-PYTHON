# Pie Chart
# Enrollment Number : 92400527159 Name : Pratham Nichani

import matplotlib.pyplot as plt

# Data
brands = ["Apple", "Samsung", "Xiaomi", "OnePlus", "Others"]
market_share = [30, 25, 20, 15, 10] # In percentage

# Creating a Pie Chart
plt.pie(market_share, labels=brands, autopct='%1.1f%%', startangle=140, colors=['red', 'blue', 'orange', 'green', 'purple'])

# Adding Title
plt.title("Market Share of Mobile Brands")

# Show the plot
plt.show()
