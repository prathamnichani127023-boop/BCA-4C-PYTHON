# income tax 

fullincome = float(input("Enter your annual income : "))

# Investments / Deductions
li = float(input("Enter your life insurance amount : "))
hi = float(input("Enter your health insurance amount : "))
tp = float(input("Enter your term plan amount : "))
fd = float(input("Enter your fixed deposit amount : "))
mf = float(input("Enter your mutual fund amount : "))
s  = float(input("Enter your stock investment amount : "))

# Total investments
inc = li + hi + tp
inv = fd + mf + s

# Standard deduction limit
if inc <= 150000:
    income = fullincome - inc
    print("No need to pay tax on investment part")
else:
    income = fullincome - 150000

tax = 0

# Tax Slabs
if income <= 400000:
    tax = 0

elif income <= 800000:
    tax = (income - 400000) * 0.05

elif income <= 1200000:
    tax = (income - 800000) * 0.10

elif income <= 1600000:
    tax = (income - 1200000) * 0.15

elif income <= 2000000:
    tax = (income - 1600000) * 0.20

elif income <= 2400000:
    tax = (income - 2000000) * 0.25

else:
    tax = (income - 2400000) * 0.30

print("Total Payable Tax :", tax)
