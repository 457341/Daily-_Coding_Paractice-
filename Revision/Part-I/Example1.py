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
n = int(input("Enter number: "))
n = str(n)
result = int(n) + int(n+n) + int(n+n+n)
print(result)