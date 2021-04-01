# # Write a Python program to display your details like name, age, address in three different lines.
# name = "Manzoor"
# surname = "Hussain"

# country = "Pakistan"
# print("Name: {}\nSurname: {}\nCountry: {}".format(name,surname,country))


# # the future value of a specified principal amount, rate of interest, and a number of years

# # Formula:  FV = P(1 + rt).
# def calculate_future_value(p,r,t):
#     print("The future value is: ",p*(1 + r*t))

# calculate_future_value(10000,3.5,7)
# # est Data : amt = 10000, int = 3.5, years = 7
# # Expected Output : 12722.79

# # Write a Python program to check whether a file exists.

# import os
# file = open('Notes.txt','r')
# print(os.path.isfile('Notes.txt'))
# print(os.path.isfile('exercise.txt'))

# # Get the current directory of current file
# print(os.path.curdir)
# print(os.getcwd)

# # For 32 bit it will return 32 and for 64 bit it will return 64
# import struct
# print(struct.calcsize("P") * 8)

# # Write a Python program to parse a string to Float or Integer.
# n = "246.2458"
# print(float(n))
# print(int(float(n)))

# # Write a Python program to print without newline or space
# print("Manzoor Hussain",end='')
# print("From Pakistan")



# # Given variables x=30 and y=20, write a Python program to print "30+20=50".

# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# print(f"{x} + {y} = {x+y}")

# # swapping two numbers
# def swap(x,y):
#     print("Previsus valuees are ",x,y)
#     temp = x
#     x = y
#     y = temp
#     print("New valuees are ",x,y)
    
# swap(x,y)


# # Write a Python program to remove the first item from a specified list.
# color = ["Red", "Black", "Green", "White", "Orange"]
# print("\nOriginal Color: ",color)
# del color[0]
# print("After removing the first color: ",color)
# print()
# # Write a Python program to input a number, if it is not a number generate an error message.

# while True:
#     try:
#         a = int(input("Enter number: "))
#         break
#     except ValueError:
#         print("This is not a number, Please try again........")

# #  Write a Python program to filter the positive numbers from a list.

# import random 
# def generate_random_num():

#     random_numbers = []
#     for i in range(1,11):
#         n = random.randint(-5,5)
#         random_numbers.append(n)
#     return random_numbers

# def filter_postive_num(list):
#     positive_num = []
#     for i in list:
#         if i > 0:
#             positive_num.append(i)
#     # print("Positive numbers are: ",positive_num)
#     return positive_num
# print(filter_postive_num(generate_random_num()))

# #  Write a Python program to compute the product of a list of integers (without using for loop)
# import math
# print("The product is: ",math.prod(filter_postive_num(generate_random_num())))
# # print(import math.prod([1,2]))




# #  Write a Python program to sum of all counts in a collections.
# import collections
# numbers = generate_random_num()
# print("There are ",sum(collections.Counter(numbers).values()),"elements in the list")



# # Write a Python program to check whether lowercase letters exist in a string
# str1 = 'A8238i823acdeOUEI'
# print(any(c.islower() for c in str1))

# Write a Python program to input two integers in a single line
a ,b= (input("Enter Numbers: ").split())
print("Entered values are: ",a,b)
