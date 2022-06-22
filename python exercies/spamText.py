text=input("Enter the text :\n")
spam=False
if("make more money" in text):
    spam=True
elif("click here" in text):
    spam=True
elif("subscribe" in text):
    spam=True

if(spam):
    print("This is a Spam Text\n")
else:
    print("This is not a Spam Text\n")
