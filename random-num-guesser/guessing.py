import random

secretNumber = random.randint(1,100)
#print(secretNumber)

guesses = 0
guess = ""

print("Welcome to the guessing game! You have up to 10 attempts to guess the number.")

while guess != secretNumber:
    guess = int(input(f"Attempt #{guesses + 1}: Guess a number between 1 to 100: "))
    guesses += 1
    if guess > secretNumber:
        print("Your guess was too high.")
    elif guess < secretNumber:
        print("Your guess was too low.")
    elif guess == secretNumber:
        print(f"You are correct the number was {secretNumber}.")
        print(f"You got it in {guesses} guess(es).")
    if guesses == 10:
        print(f"You lost unfortunately.")
        break
    

