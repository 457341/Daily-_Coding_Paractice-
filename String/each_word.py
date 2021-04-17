# Write a Python program to count the occurrences of each word in a given sentence
def count_each_word():
    string = "My name is manzoor is, and i am from Pakistan. one two one four the it hello you the from"
    string = string.split(' ')
    string = list(string)
    count_word = {}
    print(string)
    for i in string:
        count = 0
        for j in range(len(string)):
            if string[j] == i:
                count = count + 1
        # print(i,count)
        count_word[i] = count
        count = 0
    print(count_word)

count_each_word()