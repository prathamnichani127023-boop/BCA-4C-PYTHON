# function which accepts 3 arguments
#Enrollment no: 92400527159, Name: Prtham Nichani

def arithmetic(a,b,op):
    if op == '+' :
        print("addition:  ",a+b)

    elif op == '-':
        print("subtration:  ",a-b)

    elif op == '*':
        print("multiplication: ",a*b)

    elif op == '/':
        print("division:  ",a/b)

    elif op == '%' :
        print("moduls:  ",a%b)

    else :
        print("Invaild Oprator")


a = int(input("enter first number:  "))
b = int(input("enter second number:  "))
op = input("+,-,*,/,%:  ")

arithmetic(a,b,op)
