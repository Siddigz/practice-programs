def safe_divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "You can't divide by 0."

def main():
    while True:
        a = input("Please enter the first number:  ")
        b = input("Please enter the second number:  ")
        try:
            print(f"Result: {safe_divide(float(a),float(b))}")
        except ValueError:
            print("Invalid input, please enter numeric values. ")
        
        quit = input("Do you want to continue? Y or N   ")
        if quit == "N":
            break
        else:
            continue

main()