#? Question 
# 1. Write a Python program to sum all the items in a list. 
#! Answer 
lst = [1, 2, 3, 4, 5, 6]
print("Sum of list is: ",sum(lst))

#? Question 
# 2. Write a Python program to multiply all the items in a list. 
#! Answer 
def multiply(lst):
    mul = 1
    for i in lst:
        mul *= i
    return mul
print("Multiplication of list is: ",multiply(lst))

#? Question 
# 3. Write a Python program to get the largest number from a list. 
#! Answer 
def largest(lst):
    largest_number = 1
    for i in lst:
        if largest_number < i:
            largest_number = i
    return largest_number
print("Largest number in list is: ",largest(lst))
#? Question 
# 4. Write a Python program to get the smallest number from a list. 
#! Answer 
# 

#? Question 
# 5. Write a Python program to count the number of strings where the string length is 2 or more 
# and the first and last character are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

#! Answer 