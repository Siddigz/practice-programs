

def separate_numbers(originalList: list):
    nonNegatives = []
    negatives = []
    for number in originalList:
        if number < 0:
            negatives.append(number)
        else:
            nonNegatives.append(number)
    return nonNegatives, negatives 

def bubble_sort(aList: list, ascending:bool):
    quit = False
    while quit == False:
        quit = True
        for x in range(len(aList) -1):
            if ascending:
                if aList[x] > aList[x+1]:
                    temp = aList[x]
                    aList[x] = aList[x+1]
                    aList[x+1] = temp 
                    quit = False
            else:
                if aList[x] < aList[x+1]:
                    temp = aList[x]
                    aList[x] = aList[x+1]
                    aList[x+1] = temp 
                    quit = False
        
    

    return aList

    



    

def main():
    integerList = [12, 3, -7, 3, -45, 22, 8, 0, 3, -13, 3, 19, -21, 5, -9, -11, 15, 3, 30, -33, -4, 7, 25, -2, 3]
    nonNegatives, negatives = separate_numbers(integerList)
    print(f"The original list is \n{integerList}\n")


    print(f"[Ascending] Non-negative numbers sorted:\n{bubble_sort(nonNegatives, True)}\n")
    print(f"[Descending] Non-negative numbers sorted:\n{bubble_sort(nonNegatives, False)}\n")
    print(f"[Ascending] Negative numbers sorted:\n{bubble_sort(negatives, True)}\n")
    print(f"[Descending] Negative numbers sorted:\n{bubble_sort(negatives, False)}\n")











if __name__ == "__main__":
    main()