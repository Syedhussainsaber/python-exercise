names=["sadiq",'saber','Khaleel','zabi','Siddiq','Osman','Farhan']
name=input("Enter the name you want to search\n")
count=names.count(name)
if(count):
    print("Yes,this name is present in the list\n")
else:
    print("No,this name is not present in the list\n")