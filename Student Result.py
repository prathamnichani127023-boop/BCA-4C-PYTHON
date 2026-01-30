# Student result
#Enrollment no: 92400527159, Name: Prtham Nichani

mark1 = int(input("enter mark 1 :"))
mark2 = int(input("enter mark 2 :"))
mark3 = int(input("enter mark 3 :"))
mark4 = int(input("enter mark 4 :"))

total = mark1 + mark2 + mark3 + mark4
per = total / 4

print("Total: ",total)
print("Percentage:",per)

if mark1 < 40 or mark2 < 40 or mark3 < 40 or mark4 < 40:
    print("result = fail ")
    print("grade = With Held")

else:
    print("result = pass")


    if per >= 95:
        print("grade = A+ ")

    elif per >= 70:
        print("grade = B+ ")

    elif per >= 50:
        print("grade = B ")

    elif per >= 40:
        print("grade = C ")

