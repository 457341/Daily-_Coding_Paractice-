# Write a Python program to concatenate N strings.
def concat_strings(*args):
    strr = ''
    for i in args:
        strr += i
    print(strr)

concat_strings("Manzoor ","Hussain","Mughal","From","Pakistan")


# Write a Python program to test whether all numbers of a list is greater than a certain number.

numbers = [1,24,9,4]
print(all(x > 1 for x in numbers))
print(all(x < 50 for x in numbers))