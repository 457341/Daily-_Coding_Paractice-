# Write a Python program to compute sum of digits of a given string
def sum(string):

    string = list(string)
    print(string)
    total = 0
    for i in string:
        # total = total + int(i)
        total += int(i)
    print(total)
sum("123")