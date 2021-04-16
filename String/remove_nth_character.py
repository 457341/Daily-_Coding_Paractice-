# Write a Python program to remove the nth index character from a nonempty string
def remove_char(string,n):
    string  = list(string)
    string[n] = ''
    # for i in string:
    #     #
    string = ''.join(string)
    print(string)


remove_char("Manzoor",1)