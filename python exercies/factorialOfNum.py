# Factorial of the number
number=int(input("Enter the number:\n"))
fact=1
for num in range(1,number+1):
  fact=fact*num
print(fact)