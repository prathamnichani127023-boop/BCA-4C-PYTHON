# Box Float
# Enrollment Number : 92400527159 Name : Pratham Nichani

import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = [45, 48, 50, 55, 58, 60, 62, 65, 70, 75, 78, 80, 85, 88, 90, 92, 95]

# Create a box plot
plt.figure(figsize=(6, 4))
sns.boxplot(data=data)

# Show the plot
plt.title("Box Plot of Test Scores")
plt.show()
