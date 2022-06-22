num1=int(input("Enter num1:\n"))
num2=int(input("Enter num2\n"))
num3=int(input("Enter num3:\n"))
num4=int(input("Enter num4:\n"))

# num=list[num1,num2,num3,num4]
# for nums in num :
#     number=int(input("Enter the num",nums))
#     num.add(number)

if ((num1>num2)and(num1>num3)and(num1>num4)):
     print(num1,"is the greatest number\n")
elif ((num2>num3)and(num2>num4)) :
    print(num2,"is the greatest number\n")
elif((num3>num4)):
    print(num3,"is the greatest number\n")
else:
    print(num4,"is the greatest number\n")



