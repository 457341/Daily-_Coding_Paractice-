# Question 22
# Level 3

# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
def frequency_of_words(text):
    # text = dict(text)
    text = text.split(" ")
    text = list(text)
    text.sort()
    new_dict = {}
    for t in text:
        # if text.count(t) == 0:
        #     new_dict[t] = 0
        # else:
            new_dict[t] = text.count(t)
    print(new_dict)
text = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'
frequency_of_words(text)
# isim = "Manzoor"
# print(count(m))