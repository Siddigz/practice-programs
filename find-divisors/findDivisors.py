

def findDivisors(a):
    """
    Function Description:
        The purpose of this function is give all the possible divisors a number can be divided with.
    Parameters: 
        a (int): number you want to find divisors of
    Return:
        list: numbers that the input variable can be divided with 
    """
    list = []
    for i in range(1,a+1):
        if a % i == 0:
            list.append(i)
    return list

number = int(input("Please input a number to find the divisors of:  "))

print(f"{number} is divisible by: {findDivisors(number)}")