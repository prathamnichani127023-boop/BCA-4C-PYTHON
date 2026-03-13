# Factorial using Function
#Enrollment no: 92400527159, Name: Prtham Nichani

def factorial(num):
    fact = 1
    

    for i in range(1,num+1):
        fact = fact * i
    print("fact is : ",fact)


num = int(input("Enter number: "))
factorial(num)
    
