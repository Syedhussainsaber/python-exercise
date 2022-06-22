def countWord(word,fileContent):
    count=fileContent.count(word)
    if (count):
        return print("Yes it is present in the file")
    else:
        return print("No it is not present in the file")

with open("poem.txt","r") as file :
    f=file.read()
    print(f)
    presentOrNot=countWord("twinkle",f)
    

