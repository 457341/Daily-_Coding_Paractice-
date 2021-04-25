# Write a Python program to count repeated characters in a string. 
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :


def count_repeated_char(string):

    count_repeated = {}
    string = list(string)
    for i in string:
        if i in string:
            count_repeated[i] = count_repeated[i] + 1
        else:
            count_repeated[i] = 1

    print(count_repeated)


string = 'thequickbrownfoxjumpsoverthelazydog'
count_repeated_char(string)