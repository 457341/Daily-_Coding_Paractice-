# 16. Write a Python program to get the difference between a given number and 17,
#  if the number is greater than 17 return double the absolute difference.
given_number = int(input("Enter the number: "))
n = 16
if abs(given_number) > n:
    print(2*abs(given_number))
else:
    print("Given number is smaller:")

     