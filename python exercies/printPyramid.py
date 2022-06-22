number=int(input("enter the number:\n"))
for i in range(number):
    print(" " *(number-i),end='')
    print("*"*(2*i+1),end='')
    print(" "*(number-i))
