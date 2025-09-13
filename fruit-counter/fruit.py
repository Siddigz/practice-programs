    

def count_fruit(fruit_list):
    fruit_count = {}
    for fruit in fruit_list:
        if fruit in fruit_count:
            fruit_count[fruit] += 1
        else:
            fruit_count[fruit] = 1
    
    return fruit_count


def main():
    fruits = ["apple", "banana", "apple", "orange", "banana", "apple", "grape", "orange"]
    print(count_fruit(fruits))

main()