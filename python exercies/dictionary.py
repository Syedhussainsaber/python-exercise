myDict={
    "Name":"Syed Hussain Saber",
    "Roll-No":"20eg101238"
}
print(myDict.get("Name")) #Display the value inside the key
print(myDict.items()) # Display the items in the dictionary as list
print(myDict.values()) #Display the value in the form list
print(myDict.get("Saber")) #Display none
# print(myDict.get("Roll-No"))      #diplay the value in the key 
myDict.update({    # Adds the given Dict to the existing dict 
    "Branch":"Civil",
    "Section":"2B"
})
print(myDict)