# Write a Python program to extract a given number of randomly selected elements from a given list. 
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Selected 3 random numbers of the above list:
# [4, 4, 1]
import random
def select_random(list,n):
    return random.sample(list,n)

list =[1, 1, 2, 3, 4, 4, 5, 1]
print(select_random(list,3))
