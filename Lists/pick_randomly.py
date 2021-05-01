#  Write a Python program to select an item randomly from a list
import random
def pick_randomly(list):
    # for i in list:
    print(random.choice(list))
list = [1,2,3,4,5,6,7,8,9]
pick_randomly(list)

