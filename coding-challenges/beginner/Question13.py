# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
def count_letters_and_digits(input):
    digit_count = 0
    alpha_count = 0
    input = list(input)
    print(input)
    for i in input:
        if i.isdigit():
            digit_count +=1
        if i.isalpha():
            alpha_count +=1
    print("Total digits: ",digit_count)
    print("Total letters: ",alpha_count)
count_letters_and_digits("hello world! 123")
