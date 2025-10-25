

def checkError(int):
    if int < 2:
        print("Looks like we've got a baby tree here - not quite ready for Christmas cheer.")
        return True
    elif int > 10:
        print("Whoa, that tree is too big for my cozy living room. Let's find one that fits just right.")
        return True
    else:
        return False


def generateTree(height):
    for x in range(height):
        print(("*"*(2*x+1)).center(height*2))
    print("|".center(height*2))


while True:
    height = input("Enter the height of the Christmas tree (type quit to quit): ")
    if height.upper() == "QUIT":
        break
    else:
        height = int(height)
        if checkError(height) == True:
            pass
        else:
            generateTree(height)


