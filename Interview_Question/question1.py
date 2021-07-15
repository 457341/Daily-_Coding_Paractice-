# Suppose you are given a tuple containing ints and strings. Write a Python function to return the # of times a
# given element, n, appears in the tuple.
# For example, given the tuple below, where n=3, your function should return 4, since 3 appears 4 times in the
# tuple
# input:
#  n = 3
#  my_tuple = 2, 'my_string', 4, 3, 3, 3, 2, 3
# output:
#  4
n = 3
my_tuple = 2, 'my_string', 4, 3, 3, 3, 2, 3

total_number = my_tuple.count(3)
print (total_number)

# Question 2 - Counting capital letters
# Using Python, write code that will read a file and return the number of capital letters.
# Once you have your initial piece of code, see if you can condense into a one-liner.
f = open("D:\Python (Don't break the chain)\Interview_Question\info.txt", 'r')
print(f.readlines())
for line in f:
    print(line)