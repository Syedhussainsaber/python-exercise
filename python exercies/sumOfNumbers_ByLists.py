numbersList=[]
print("Enter The 4 Numbers U Want To Add :")
i=0
while i<4 :
  Number=int(input())
  numbersList.append(Number)
  i=i+1
sum=0
i=0
for numbers in numbersList:
 sum=sum+numbersList[i]
 i=i+1
print("\nThe Sum Of The 4 Numbers is",sum)

# Counting an element in the tuple
a=(1,23,3,0,4,0,5,0,2,0,0)
print("\n",a.count(0))