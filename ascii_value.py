#  Write a Python program to get the ASCII value of a character
import string
print(ord('a'))

for i in string.ascii_uppercase:
    print(f'Ascii value of {i} is: {ord(i)}') # it is a different usage of pirnt function
    # print('Ascii value of {} is: {}'.format(i,ord(i)))

print("-"*40)
for i in string.ascii_letters: # all lowers and upper letters
    print('Ascii value of {} is: {}'.format(i,ord(i)))
