from datetime import date
letter='''Dear <Name>,\nYou are selected! \n<Date>'''
name=input("Enter your name\n")
Date = date.today()
letter=letter.replace("<Name>",name)
letter=letter.replace("<Date>",str(Date))
print(letter)
