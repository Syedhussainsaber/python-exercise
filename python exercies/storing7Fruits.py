from ast import For
from re import S

fruits=[]
i=0
print("Enter the fruits")
while i<7:
 fruit=input()
 fruits.append(fruit)
 i=i+1
print("\n")
for x in fruits :
 print(x)