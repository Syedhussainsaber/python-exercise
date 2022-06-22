n=int(input("Enter the number\n"))
j=n-1
while(j>0):
    print(" "*j+"*"*(2),end='')
    j=j-1


for i in range(n+1):
    print("*"*(2*i-1))