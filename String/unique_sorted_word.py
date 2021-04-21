#  Write a Python program that accepts a comma separated sequence of words as input and
#   prints the unique words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red


# Funtion 1
def sort_unique_words1(string):
    # print(string)
    string = string.split(',')
    print(string)
    unique_words = {}

    # string= sorted(string)
    for i in string:
        if i in unique_words:
            unique_words[i] = ''
        else:
            unique_words[i] = 1
    unique_words = list(unique_words)
    print(' '.join(sorted(unique_words)))



# str = input("Enter words: ")
str = "red,white,black,red,green,black"
print("Using Funtion 1: ")
sort_unique_words1(str)



