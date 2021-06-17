# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
def remove_duplicates(text):
    #! first Approch
    # lst = set(text.split(" "))
    # lst = list(lst)
    # lst.sort()
    # print(lst)
    #! Second Approch
    # text = sorted(list(set(text.split(" "))))
    # text = ' '.join(text)
    #! Third Approch
    text = ' '.join(sorted(list(set(text.split(" "))))) # It is also true
    print(text)
text = "hello world and practice makes perfect and hello world again"
remove_duplicates(text)