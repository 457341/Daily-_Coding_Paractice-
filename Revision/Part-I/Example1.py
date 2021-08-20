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
