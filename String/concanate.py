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

#  Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Go to the editor
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

# print('string'.endswith('ing'))
def add_ing_or_ly(string):
    intitial_str = string
    if len(string) >= 3:
        if string.endswith("ing"):
            string = string+ "ly"
        else:
            string = string + "ing"
        print(f"The result of '{intitial_str}' is: {string}")
    else:
        print("The length of string must be atleast 3. Try again")
        while(True):
            string = input("Enter string with aleast length of 3: ")
            if len(string) >=3:
                add_ing_or_ly(string)
                break


add_ing_or_ly("abc")
add_ing_or_ly("string")
add_ing_or_ly("ab")