
def printLists(customersList):
    for customer in customersList:
        printIndividualList(customer)
        print()

def printIndividualList(customer):
    if customer[1] == "G":
        print(f"{customer[0]} has a gold discount of 10%, order of ${customer[2]} is discounted for ${(customer[2] * 0.1):.2f} for a final total of ${(customer[2]-(customer[2] * 0.10)):.2f}")
    elif customer[1] == "S":
        print(f"{customer[0]} has a silver discount of 5%, order of ${customer[2]} is discounted for ${(customer[2] * 0.05):.2f} for a final total of ${(customer[2]-(customer[2] * 0.05)):.2f}")
    elif customer[1] == "B":
        print(f"{customer[0]} has a bronze discount of 2%, order of ${customer[2]} is discounted for ${(customer[2] * 0.02):.2f} for a final total of ${(customer[2]-(customer[2] * 0.02)):.2f}")
    else:
        print("Error 1")

def main():
    customerRecords = [["Sean Benjamin", "B", 30.22], ["Yanan Mao", "G", 40.22], ["Charlie Brown", "S", 22.30], ["Snoopy Dog", "G", 69.33], ["Woodstock Bird", "S", 25.00]]
    printLists(customerRecords)

if __name__ == "__main__":
    main()

