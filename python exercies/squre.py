number=int(input("Enter the number\n"))
for i in range(number):
    if(i==0)or(i==number-1):
        print("* "*number+'\n',end='')
    else:
        print("*"+' '*(2*number-3)+"*\n",end='')