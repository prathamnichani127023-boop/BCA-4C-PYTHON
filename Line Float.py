# Line Float
# Enrollment Number : 92400527159 Name : Pratham Nichani

import matplotlib.pyplot as plt


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
temperature = [30, 32, 34, 33, 31, 29, 28]

plt.plot(days, temperature, marker='o', linestyle='-', color='b', label="Temperature")


plt.xlabel("Days of the Week")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trend Over a Week")
plt.legend() 
plt.grid(True) 
plt.show()
