#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return instead of the empty string.

def concat_string(string):
    first_two = string[0] + string[1]
    last_two = string[-2] + string[-1]
    result = first_two + last_two
    print(f"The result is: {result}")
concat_string("Manzoor") # result should be: Maor
