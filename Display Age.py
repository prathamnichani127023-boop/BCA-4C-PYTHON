# Display  Age
#Enrollment no: 92400527159, Name: Prtham Nichani

age = int(input("enter age: "))

if age < 12:
    print("You are Kid")

elif age >= 12 and age <= 17:
    print("You are Teenager")

elif age >= 18 and age <= 60:
    print("You are Adult")

else:
    print("You are a Senior Citizen")

