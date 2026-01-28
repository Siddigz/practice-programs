# numbers = [1,3,3,9,5,7,8,2,10,8,4,1]

def replacer(old,word,numList):
    '''replaces similar elements with new elements in the same locations

    args:
        old (int): original element to be replaced
        word (string): new word to take place in place of old integer
        numList (list): list that changes take place in
        
    returns:
        formatted string: new list with replaced elements
    '''
    rep = 0
    for x in range(numList.count(old)):
        numList.insert(numList.index(old), word)
        numList.remove(ans)
        rep += 1
    print(f"List: {numList}")
    return rep

numbers = []
while True:
    listNumber = int(input("Please enter a list of numbers from 1 to 10. (Input -1 to end list)\t"))
    if listNumber == -1:
        break
    numbers.append(listNumber)

print(f"The list is {numbers}")


while True:
    ans = input("Enter a number to replace ['q' to quit]>> ")
    if ans.upper() == "Q":
        break
    word = input("with string>> ")
    ans = int(ans)
    rep = replacer(ans,word,numbers)
    print(f"The number {ans} was replaced {rep} times.")