# Bar float
# Enrollment Number : 92400527159 Name : Pratham Nichani

import matplotlib.pyplot as plt


products = ["Laptop", "Mobile", "Tablet", "Headphones", "Smartwatch"]
sales = [150, 300, 100, 180, 120]

plt.bar(products, sales, color='green')

plt.xlabel("Products")
plt.ylabel("Sales (Units)")
plt.title("Sales of Different Products")


plt.show()
