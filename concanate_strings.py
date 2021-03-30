# Write a Python program to concatenate N strings.
def concat_strings(*args):
    strr = ''
    for i in args:
        strr += i
    print(strr)

concat_strings("Manzoor ","Hussain","Mughal","From","Pakistan")


