# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
def count_upper_lower_case_letters(text):
    # input = list(input)
    print(text)
    # text = list(text)
    print(text)
    count_uppercase = 0
    count_lowercase = 0
    for letter in text:
        if letter.isupper():
            count_uppercase += 1
        if letter.islower():
            count_lowercase += 1
    print("Upper Case: " ,count_uppercase)
    print("Lower Case: " ,count_lowercase)



count_upper_lower_case_letters("Hello world!")