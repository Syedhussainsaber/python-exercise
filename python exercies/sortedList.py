marks=[]
i=0
print("Enter the marks of the students")
while i<6 :
 studentMark=int(input())
 marks.append(studentMark)
 i=i+1
print("\n")
j=0
for studentMarks in marks:
 marks.sort()  
 print(marks[j])
 j=j+1