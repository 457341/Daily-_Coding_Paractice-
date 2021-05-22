# Write a Python program that accepts a string and calculate the number of digits and letters
def calculate_no_of_digits(data):
    digits = []
    alphabets = []
    for i in range(len(data)):
        if data[i].isalpha():
            alphabets.append(data[i])
        if data[i].isdigit():
            digits.append(data[i])
    print("Total digits: ",len(digits) ," and total alphabets: ",len(alphabets))

data = input("input data: ")
# print(data)
calculate_no_of_digits(data)
