# prime number or not
#Enrollment no: 92400527159, Name: Prtham Nichani


num = int(input("enter number:  "))

flag = 0 
for i in range(2,num):
        if num % i == 0 :
            flag = 1
            break
if flag == 1 :
    print("not prime")

else :
        print("prime") 
