# Write a Python program to count repeated characters in a string. 
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2


def count_repeated_char(string):

    count_repeated = {}
    # string = list(string)
    for i in string:
        if string.count(i) >1:
            count_repeated[i] = string.count(i)
        # print("Element: ",i,"= ",count)

    for i in count_repeated:
        print(f'{i}: {count_repeated[i]}') 



string = 'thequickbrownfoxjumpsoverthelazydog'
# string2 = "manzoorhussain"
count_repeated_char(string)
# print(string2.count('a'))