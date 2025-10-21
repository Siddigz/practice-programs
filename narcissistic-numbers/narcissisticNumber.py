

print("Please input the range of numbers to find the Narcissistic numbers within.")
quit = False

while quit != True:
    start = 0
    end = ""
    if quit != True:
        while len(str(start)) != 3 or (int(start) < 100):
            start = input("Input the start of the range or enter ""q"" to exit the program. (Your number should consist of 3 digits)\t")
            if start.upper() == "Q":
                quit = True
                break
            elif len(start) == 3 and int(start) >= 100:
                    start = int(start)
                    break
            print("Invalid Number")

    if quit != True:
        while len(end) != 3:
            end = input("Input the end of the range or enter ""q"" to exit the program. (Your number should consist of 3 digits)\t")
            if end.upper() == "Q":
                quit = True
                break
            elif len(end) == 3:
                end = int(end)
                break
            print("Invalid Number")




        if quit != True:
            for i in range(start,end+1):
                if (i//100)**3 + ((i%100)//10)**3 + (i%10)**3 == i:
                    print(i)


    