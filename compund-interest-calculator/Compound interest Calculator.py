while True:
    principal = int(input("Input principal amount:\n"))
    if principal < 0:
        print("Principal can't be less than zero.")
    else:
        break

while True:
    rate = float(input("Input rate amount:\n"))
    if rate < 0:
        print("Rate can't be less than zero.")
    else:
        break

while True:
    time = int(input("Input timeframe:\n"))
    if time < 0:
        print("time can't be less than zero.")
    else:
        break    






final = principal * pow((1+(rate/100)),time)

print(f"Final ammount after {time} years is ${final:.2f}.")
