import displayCustomer

def createRecord():
    customerInfo = []
    customerInfo.append(input("What is the customer's name? "))
    customerInfo.append(input("Discount type? "))
    customerInfo.append(float(input("Cost of the order? ")))
    return customerInfo

def main():
    number = int(input("How many customers do you want to add? "))
    customersList = []
    for x in range(number):
        customersList.append(createRecord())
    displayCustomer.printLists(customersList)


if __name__ == "__main__":
    main()

