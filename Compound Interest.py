# Compound Interest

p = float(input("Enter Amount: "))
r = float(input("Enter Rate : "))
t = float(input("Enter Time : "))

ci = p * (1 + r / 100) ** t - p

print("Compound Interset: ", ci)
