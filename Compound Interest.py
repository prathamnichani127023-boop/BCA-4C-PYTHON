# Compound Interest
#Enrollment no: 92400527159, Name: Prtham Nichani

p = float(input("Enter Amount: "))
r = float(input("Enter Rate : "))
t = float(input("Enter Time : "))

ci = p * (1 + r / 100) ** t - p

print("Compound Interset: ", ci)
