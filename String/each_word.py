# Write a Python program to count the occurrences of each word in a given sentence
def count_each_word(string):
    
    string = string.split(' ')
    string = list(string)
    count_word = {}
    # print(string)
    for i in string:
        count = 0
        for j in range(len(string)):
            if string[j] == i:
                count = count + 1
        # print(i,count)
        count_word[i] = count
        count = 0
    print(count_word)

def count_each_word2(string): # a better solution for upper function
    string = string.split(' ')
    count_word = {}
    # print(string)
    for i in string:
        # count = 0
        if i in count_word:
            count_word[i] += 1
        else:
            count_word[i] = 1
        
    print(count_word)
string1 = "My name is manzoor is, and i am from Pakistan. one two one four the it hello you the from"
string2 = "One two One four five six two Five"
count_each_word(string1)
count_each_word(string2)
count_each_word2(string1)
count_each_word2(string2)