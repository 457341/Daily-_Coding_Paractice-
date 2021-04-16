# Write a Python program to remove the nth index character from a nonempty string
def remove_char(string,n):
    string  = list(string)
    string[n] = ''
    # for i in string:
    #     #
    string = ''.join(string)
    print(string)

def remove_char2(string,n):
    first_part = string[:n]
    second_part = string[n+1:]

    print(f'The result of {string} after {n}th index deleting is: {first_part + second_part}')

remove_char("Manzoor",1)
remove_char2("Manzoor",5)