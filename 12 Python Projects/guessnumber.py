# Task: Below are the steps:

# Build a Number guessing game, in which the user selects a range.
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses
import random
first, last = [int(x) for x in input("Enter a range: ").split()]
# print(first + last)
random_number = random.randint(first, last)
print("Random number: " ,random_number)
guessed = int(input("Guess n number: "))
counter = 0
while(True):
    counter += 1
    if guessed > random_number:
        
        last = guessed
        print("you guessed too highg: ")
        print("Guess between: ",first, last)
    if guessed < random_number:
        print("you guessed too low: ")
        first = guessed
        print("Guess between: ",first, last)
    if guessed == random_number:
        print("you guessed correctly: ",guessed, "in" , counter," times.")
        break
    guessed = int(input("Guess again: "))