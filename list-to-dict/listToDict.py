



def listToDictionary(aList):
    dict = {}
    for list in aList:
        if list[0] in dict:
            (a,b) = dict[list[0]]
            b += list[2]
            c = []
            for item in a:
                c.append(item)
            c.append(list[1])
            dict[list[0]] = [c,b]
        else:
            dict[list[0]] = [[list[1]],list[2]] 
    return dict

def display(aDictionary):
    for customer in aDictionary:
        print(f"{customer} : {aDictionary[customer]}")



def main():

    
    sales = [ ["customer1", "bread", 5], ["customer2", "bread", 4.5], 
    ["customer1", "egg", 6.75], ["customer2", "milk", 4.35], 
    ["customer3", "egg", 3.6], ["customer4", "bread", 4.5], 
    ["customer1", "milk", 4.35], ["customer2", "egg", 3.6], 
    ["customer4", "milk", 4.35] ]


    dictCustomers = listToDictionary(sales)
    display(dictCustomers)

if __name__ == "__main__":
    main()