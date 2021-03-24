# Write a Python program to calculate the sum of three given numbers, 
# if the values are equal then return three times of their sum
def sum(a,b,c):
    total_sum = a + b + c
    if a == b == c:
        total_sum = total_sum*3
    return a + b +c
print("Total sum is: ",sum(3,3,5))
print("Total sum is: ",sum(2,2,2))