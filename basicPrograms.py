# # # Write a Python program to display your details like name, age, address in three different lines.
# # name = "Manzoor"
# # surname = "Hussain"

# # country = "Pakistan"
# # print("Name: {}\nSurname: {}\nCountry: {}".format(name,surname,country))


# # # the future value of a specified principal amount, rate of interest, and a number of years

# # # Formula:  FV = P(1 + rt).
# # def calculate_future_value(p,r,t):
# #     print("The future value is: ",p*(1 + r*t))

# # calculate_future_value(10000,3.5,7)
# # # est Data : amt = 10000, int = 3.5, years = 7
# # # Expected Output : 12722.79

# # # Write a Python program to check whether a file exists.

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



# Given variables x=30 and y=20, write a Python program to print "30+20=50".

x = int(input("Enter x: "))
y = int(input("Enter y: "))
print(f"{x} + {y} = {x+y}")

# swapping two numbers
def swap(x,y):
    print("Previsus valuees are ",x,y)
    temp = x
    x = y
    y = temp
    print("New valuees are ",x,y)
    
swap(x,y)


# Write a Python program to remove the first item from a specified list.
color = ["Red", "Black", "Green", "White", "Orange"]
print("\nOriginal Color: ",color)
del color[0]
print("After removing the first color: ",color)
print()
# Write a Python program to input a number, if it is not a number generate an error message.

while True:
    try:
        a = int(input("Enter number: "))
        break
    except ValueError:
        print("This is not a number, Please try again........")