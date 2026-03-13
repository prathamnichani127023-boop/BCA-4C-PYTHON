# Print all prime numbers between 1 to 100.
#Enrollment no: 92400527159, Name: Prtham Nichani

for num in range(1, 101):
    
    if num > 1:
        flag = 0   
        
        for i in range(2, num):
            if num % i == 0:
                flag = 1   
                break
        
        if flag == 0:
            print(num, end=" ")
