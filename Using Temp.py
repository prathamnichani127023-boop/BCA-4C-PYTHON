# Using Temp

a=int(input("enter first number:  "))
b=int(input("enter second number:  "))


print("before swampping:  ")
print("first value:  ",a)
print("second value:  ",b)

temp = a
a=b
b=temp

print("after swapping:  ")
print("first value:  ",a)
print("second value:  ",b)
