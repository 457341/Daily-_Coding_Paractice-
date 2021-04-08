# This program is about to guess a number, if guess number is equal to 
# randomly generated number, try again
import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while(guess!=random_number):
        guess = int(input("Guess a number between 1 and {}: ".format(x)))
        if random_number>guess:
            print("Number is too high, try again")
        elif random_number < guess:
            print("Number is too low, try again.")
    print(f"Congratulations you guessed the number {random_number} correctly.")
guess(10)