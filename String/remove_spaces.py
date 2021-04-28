# Write a Python program to remove spaces from a given string.
def remove_space(string):

    # string = list(string)
    string = string.split()
    print(string)
    string = ''.join(string)
    print(string)
string = "manzoor hussain mughal"

remove_space(string)