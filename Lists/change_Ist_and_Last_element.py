# Given a list, write a Python program to swap first and last element of the list.

# Examples: 

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]
lst = [12, 35, 9, 56, 24]
temp = lst[0]
lst[0] = lst[-1]

lst[-1] = temp
print(lst)