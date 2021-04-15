#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return instead of the empty string.

def concat_string(string):
    first_two = string[0] + string[1]
    last_two = string[-2] + string[-1]
    result = first_two + last_two
    print(f"The result is: {result}")
concat_string("Manzoor") # result should be: Maor


# Write a Python program to get a string from a given string where all occurrences of its
#  first char have been changed to '$', except the first char itself. 
# Sample String : 'restart'
# Expected Result : 'resta$t'

def change_str(string):
    original_str = string
    lst = list(string)
    first_chr = string[0]
    for i in range(1,len(lst)):
        if lst[i] == first_chr:
            lst[i] = "$"
    print(f"The result of '{original_str}' is: {''.join(lst)}")
change_str("restart")
change_str("successful")

# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
def get_single_string(strings):
    strings = strings.split(',')
    # print(strings)
    # strings = ''.join(strings)
    strings = strings[-1] + ' ' + strings[0]
    print(strings)

get_single_string(strings)