marks=int(input("Enter your marks:\n"))
if(marks>=90)and(marks<=100):
    print("O-Outstanding\n")
elif(marks>=80)and(marks<90):
    print("A-Amazing")
elif(marks>=70)and(marks<80):
    print("B-Better")
elif(marks>=60)and(marks<70):
    print("C-cool") 
elif(marks>=50)and(marks<60):
    print("D-done") 
else:
    print("You are Fail")