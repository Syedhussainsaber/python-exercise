import random
comp = None
randNo = random.randint(1, 3)
if(randNo == 1):
    comp = 's'
elif(randNo == 3):
    comp = 'w'
else:
    comp = "g"


def gameWin(you, comp):
    if comp == "s":
        if you == "w":
            return False
        elif(you == "g"):
            return True
        else:
            return None

    elif (comp == "w"):
        if you == "g":
            return False
        elif(you == "s"):
            return True
        else:
            return None

    elif (comp == "g"):
        if you == "s":
            return False
        elif(you == "w"):
            return True
        else:
            return None


you = input("Enter Snake(s),Gun(g) and Water(w)\nYours Turn:  ")
print("Computer's Turn")
print(f"You Chose {you}")
print(f"You Chose {comp}")
a = gameWin(you, comp)
if(a == None):
    print("Game Tied\n")
elif(a):
    print("You Won The Game")
else:
    print("You Lose The Game")
