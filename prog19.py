#  Write a Python program to get a new string from a given string where "Is" 
#  has been added to the front. If the given string already
#   begins with "Is" then return the string unchanged

given_string = (input("Enter the string: "))
if given_string.startswith("Is"):
    print(given_string)
else:
    print("Is "+given_string)
 Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged