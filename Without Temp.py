# Without Temp

a=int(input("enter first number:  "))
b=int(input("enter second number:  "))


print("before swampping:  ")
print("first value:  ",a)
print("second value:  ",b)

a,b=b,a

print("after swapping:  ")
print("first value:  ",a)
print("second value:  ",b)
