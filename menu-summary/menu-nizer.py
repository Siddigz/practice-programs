menu = ["Ice Cream", 3.67, 2, "Donuts", 2.50, 6, "Roll", 7.89, 3, "Pizza", 13.45, 5, "Fish and Chips", 15.20, 23, "Poutine", 8.51, 13, "Tacos", 3.00, 19]

foodItems = menu[::3]
prices = menu[1::3]
quantities = menu[2::3]

totalLength = 0
for x in foodItems:
    length = int(len(x))
    totalLength += length
meanFood=int(totalLength/len(foodItems))


updatedPrices = []
for x in range(len(prices)):
    updatedPrices.insert(x, (round(prices[x]*quantities[x], 2)))

newQuantities = []
for x in quantities:
    newQuantities.append(chr(ord("@")+x))

print(f"The mean length of the items names is {meanFood}")
print("Menu Order Summary: (Food Name: Price, Quanitity)")
for x in range(len(prices)):
    print(f"\t {foodItems[x]}: {updatedPrices[x]}, {newQuantities[x]}")




print("Done.")
