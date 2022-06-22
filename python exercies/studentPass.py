marks=[]
i=0
while i<3:
    mark=int(input("Enter marks of subject "+str(i)+' :\n'))
    marks.append(mark)
    if((marks[i]>100)or(marks[i]<0)) :
      print("Enter the correct marks\n")
      break
    i=i+1
if((marks[0]<100)and(marks[1]<100)and(marks[2]<100)) :
   avg=(marks[0]+marks[1]+marks[2])/3
   if((marks[0]<37)and(marks[1]<37)and(marks[2]<37)) :
       print("You failed in all subjects")
   elif((marks[0]<37)and(marks[1]<37)and(marks[2]>37)):
       print("You failed in subject1 and subject2\nYou passed in subject3")
   elif((marks[0]<37)and(marks[1]>37)and(marks[2]<37)):
       print("You failed in subject1 and subject3\nYou passed in subject2")
   elif((marks[0]>37)and(marks[1]<37)and(marks[2]<37)):
       print("You failed in subject2 and subject3\nYou passed in subject1")
   elif((marks[0]>37)and(marks[1]>37)and(marks[2]>37)):
    print("You passed in all 3 subjects\n")
   elif((marks[0]<37)and(marks[1]>37)and(marks[2]>37)):
    print("You failed in subject1\nYou passed in subject2 and subject3")
   elif((marks[0]>37)and(marks[1]<37)and(marks[2]>37)):
    print("You failed in subject2\nYou passed in subject1 and subject3")
   elif((marks[0]>37)and(marks[1]>37)and(marks[2]<37)):
    print("You failed in subject3\nYou passed in subject1 and subject2")
   print("Your overall Average is ",avg)
