

def loadData():
    while True:
        try:
            fileName = input("Which file do you want to load? ")
            file = open(fileName , "r")
            file = file.read()
            list = file.split("\n")
            break
        except FileNotFoundError:
            print("File not found")
    splitList = []
    for line in list:
        newLine = line.split(",")
        splitList.append(newLine)
    
    return splitList


def displayList(list:list):
    if len(list) == 0:
        print("List is empty!")
    else:
        for line in list:
            print(line)
    
    


def getSecretIngredient(recipes:list):
    secret_ingredient_dict = {}
    
    for recipe in recipes:
        if recipe[0] == "ID":
            pass
        else:
            if recipe[3] in secret_ingredient_dict:
                tempList = secret_ingredient_dict[recipe[3]]
                tempList.append(recipe[0])
                secret_ingredient_dict[recipe[3]] = tempList
            else:
                tempList = []
                tempList.append(recipe[0])
                secret_ingredient_dict[recipe[3]] = tempList


    return secret_ingredient_dict


def displayDict(dictionary:dict):
    if len(dictionary.keys()) == 0:
        print("Dictionary is empty!")
    else:
        for key in dictionary.keys():
            print(f"{key}: {dictionary[key]}")



def main():
    recipe_data = loadData()
    displayList(recipe_data) 
    print()
    secret_ingredient_dict = getSecretIngredient(recipe_data)
    displayDict(secret_ingredient_dict)





if __name__ == "__main__":
    main()