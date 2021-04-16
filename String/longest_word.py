# 8. Write a Python function that takes a list of words and returns the longest word and the length of the longest one. Go to the editor
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9
def find_longest_word(list):
    length = 0
    longest_word  = ''
    for i in list:
       # length = len(i)
        if len(i) > length:
            length = len(i)
            longest_word = i
    print(f'The longest word is {longest_word} with {length} length')
find_longest_word(["Man","Zoor","Mughal"])