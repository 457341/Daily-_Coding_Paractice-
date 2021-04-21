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

#Funtion 2
def sort_unique_words2(string):
    string = string.split(",")
    print("Original String: ",end='')
    print(string)
    str_lst = []
    for i in string:
        # print(string.count(i))
        if str_lst.count(i) == 0:
            str_lst.append(i)

    print(' '.join(sorted(str_lst)))


# Funtion 3
def sort_unique_words3(string):
    words = [word for word in string.split(",")]
    print(",".join(sorted(list(set(words)))))

# str = input("Enter words: ")
str = "red,white,black,red,green,black"
print("Using Funtion 1: ")
sort_unique_words1(str)
print("Using Funtion 2: ")
sort_unique_words2(str)
print("Using Funtion 3: ")
sort_unique_words3(str)

