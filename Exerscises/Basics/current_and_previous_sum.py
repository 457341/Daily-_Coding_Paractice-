# Write a program to iterate the first 10 numbers and in each iteration, 
# print the sum of the current and previous number.

# Printing current and previous number sum in a range(10)
# Current Number 0 Previous Number  0  Sum:  0
for i in range(10):
    current = i
    previous = i-1
    if i == 0:
        current = i
        previous = i
    sum = current + previous
    print("Current Number: ", current, "Previous Number: ",  previous , "Sum: ", sum)