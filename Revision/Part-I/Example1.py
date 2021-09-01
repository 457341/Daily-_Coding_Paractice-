# # Write a Python program to get the Python version you are using
# import sys
# print(sys.version)
# #  Write a Python program to display the current date and time.
# import datetime
# print(datetime.datetime.now())

# # Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
# # Sample data : 3, 5, 7, 23
# # Output :
# # List : ['3', ' 5', ' 7', ' 23']
# # Tuple : ('3', ' 5', ' 7', ' 23')

# numbers = input("Enter the number of numbers: ").split(',')
# print(numbers)
# print(numbers)
# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615
# n = int(input("Enter number: "))
# n = str(n)
# result = int(n) + int(n+n) + int(n+n+n)
# print(result)


# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.
# Click me to see the sample solution

# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.
# Click me to see the sample solution
#! Answer
# import calendar
# year = int(input("Enter the year: "))
# month = int(input("Enter the month: "))
# print(calendar.month(year, month))
#? Question
# 13. Write a Python program to print the following 'here document'. Go to the editor
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# Click me to see the sample solution

#? Question
# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
#! Answer :
# from datetime import date
# last_date = date(2014, 7, 2)
# first_date = date(2014, 7,11)
# difference = first_date - last_date
# print("Todal days: " , difference) # days along with hours
# print("Todal days: " , difference.days) # Only days

# Click me to see the sample solution

#? Question
# 15. Write a Python program to get the volume of a sphere with radius 6.
# Click me to see the sample solution

#? Question
# 16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference. Go to the editor
# Click me to see the sample solution

#? Question
# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000. Go to the editor
# Click me to see the sample solution.
# #! Answer:
# number = int(input("Number: "))
# if number >= 100 and number <=1000:
#     print("number is between 100 and 1000")
# else:
#     print("number is in different range")

#? Question
# Write a Python program to count the number 4 in a given list.
#! Answer:
# lst = [1,24,35,6,4,0,4]
# count_number4 = 0
# for i in lst:
#     if i == 4:
#         count_number4 +=1
# print(count_number4)
#? Question
# Write a Python program to test whether a passed letter is a vowel or not.
#! Answer
# def is_vowel(letter):
#     all_vowels= "aeiouAEIOU"
#     if letter in all_vowels:
#         print(letter, "is vowel")
#     else:
#         print(letter, "is not vowel")
# is_vowel("M")
# is_vowel("A")
#? Question
# Write a Python program to check whether a specified value is contained in a group of values. Go to the editor
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False
#! Answer
# def is_contained(lst,value):
#     if value in lst: return "Yes"
#     else: return "No"
# print(is_contained([1,5,8,3],3))
# print(is_contained([1,5,8,3],-1))
#? Question
# Write a Python program to create a histogram from a given list of integers.
#! Answer
# def make_histogram(lst):
#     for i in lst:
#         print("*"*i)
# make_histogram([1,2,3,4,5,1,2,3,4])
# make_histogram([1,2,3,4,5,4,3,2,1])
#? Question
# Write a Python program to concatenate all elements in a list into a string and return it
#! Answer
# def concatenate_all(lst):
#     all_elements = ''
#     for i in lst:
#         all_elements += str(i)
#     return all_elements
# print(concatenate_all([1,2,3,4]))
#? Question
# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5
#! Answer
# def method(int1, int2):
#     if int1 == int2 or abs(int1 - int2) == 5 or abs(int1 + int2) ==5:
#         return True
#     else:
#         return False
# print(method(2,3))
#? Question
# Calculate body mass index
#! Answer
# height = float(input("Input your height in Feet: "))
# weight = float(input("Input your weight in Kilogram: "))
# print("Your body mass index is: ", round(weight / (height * height), 2))



#? Question
#Write a Python program to calculate the sum of the digits in an integer.
# #! Answer
# def foo(num):
#     total = 0
#     while num >= 10:
#         temp = num % 10
#         total += temp
#         num = num // 10
#     total +=num
#     print(total)
# foo(1235)
# foo(12)
# foo(100)
# foo(100045)
# foo(5245)
# def lcm(x, y):
#   if x > y:
#       z = x
#   else:
#       z = y
#   while(True):
#       if((z % x == 0) and (z % y == 0)):
#           lcm = z
#           break
#       z += 1
#   return lcm
# print(lcm(4, 6))
# print(lcm(15, 17))

# #? Question 
#! Answer
# n = int(input("Input a number: "))
# sum_num = (n * (n + 1)) / 2
# print("Sum of the first", n ,"positive integers:", sum_num)

#? Question
# Write a Python program to swap two variables.
# ! Answer
# def swap(x,y):
#     temp = x
#     x = y
#     y = temp
#     return x,y
#? Question
# Write a Python program to sort three integers without using conditional statements and loops.
#! Answer
# def sort_numbers(n1,n2,n3):
#     smallest = min(n1,n2,n3)
#     biggest = max(n1,n2,n3,n1)
#     middle = (n1+n2+n3) - smallest -biggest
#     return smallest,middle,biggest
# print(sort_numbers(1,5,2))
# print(sort_numbers(0,-1,10))

#? Question
# Write a Python program to concatenate N strings
#! Answer
def concatenate_strings(*strings):
    concatenated_string = ""
    for s in strings:
        concatenated_string += s
    return concatenated_string
print(concatenate_strings("Manzoor","Hussain","Mughal"))

# ? Question
# Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary)
# ! Answer
# def sum(container):
#     total = 0
#     for c in container:
#         total += c
#     print(total)
print(sum([1,2,3,4]))
print(sum((1,2,3,4)))
print(sum({1,2,3,4}))
#? Question
#  Write a Python program to test whether all numbers of a list is greater than a certain number
#! Answer
lst = [1,2,3,4]
random_number = 3
count = 0
for i in lst:
    if i > random_number:
        count += 1
if count == len(lst):
    print("Certain number is greater than all numbers of a list")
else:
    print("Certain number is not greater than all numbers of a list")
# in built function
print(all( random_number > i for i in lst))
print(all( 5 > i for i in lst))