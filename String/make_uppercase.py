#  Write a Python function to convert a given string to all uppercase if
#   it contains at least 2 uppercase characters in the first 4 characters.
def make_uppercase(string):
    # string = string.split()
    string = list(string)
    count = 0
    for i in string[:4]:
        if i == (i).upper():
            count = count + 1
        string = ''.join(string)
        if count == 4:
            string = string.upper()
    print(string)

make_uppercase("Manzoor")
make_uppercase("PYTHOn")
make_uppercase("PROGramming")
# print("Manzoor".upper())