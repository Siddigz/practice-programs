

def sum_of_evens_non_recursive(aList):
    result = 0
    for number in aList:
        if number%2 == 0:
            result += number
    return result


def sum_of_odds_non_recursive(aList):
    result = 0
    for number in aList:
        if number%2 != 0:
            result += number
    return result



def sum_of_evens_recursive(aList):
    number = 0
    if aList == []:
        return number
    
    number = aList[0]
    
    if number%2 != 0:
        number = 0
    return number + sum_of_evens_recursive(aList[1:])
    

def sum_of_odds_recursive(aList):
    number = 0
    if aList == []:
        return number
    
    number = aList[0]
    
    if number%2 == 0:
        number = 0
    return number + sum_of_odds_recursive(aList[1:])





def main():
    contin = "Y"

    # numbers = [1,2,3,4,5,6,7,8]

    while contin.upper() == "Y":

        numbers = []
        while True:
            number = input("Enter a number (quit): ")
            if number.upper() == "QUIT":
                break
            else:
                numbers.append(int(number))
    
            

        print(f"[Non-Recursive] Sum of even numbers is {sum_of_evens_non_recursive(numbers)}.")
        print(f"[Non-Recursive] Sum of odd numbers is {sum_of_odds_non_recursive(numbers)}.")
        print(f"[Recursive] Sum of even numbers is {sum_of_evens_recursive(numbers)}.")
        print(f"[Recursive] Sum of odd numbers is {sum_of_odds_recursive(numbers)}.")

        contin = input("Do you want to repeat the process? Y/N ")





if __name__ == "__main__":
    main()