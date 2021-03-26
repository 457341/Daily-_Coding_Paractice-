# Write a Python program to sum of two given integers. However, 
# if the sum is between 15 to 20 it will return 20.

def sumOfTwoNum(num1,num2):
    total = num1 + num2
    # if  total >=15 and total <= 20:
    if total in range(15,21):
        total = 20
    return total

print("The sum is: ",sumOfTwoNum(10,20))
print("The sum is: ",sumOfTwoNum(10,6))
