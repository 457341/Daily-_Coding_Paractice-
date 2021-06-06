# 3.	Questions

#----------------------------------------#
# ! Question 1
# Level 1

# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
numbers = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        numbers.append(i)
print(len(numbers))

#! Second method
numbers2 = [numbers.append(i) for i in range(2000, 3201)  if i % 7 == 0 and i % 5 != 0 ]
print(len(numbers2))


# ! Question 2: Finding the factorial 
def find_factorial(n):
    factorial = 1
    for i in range(1,n+ 1):
        factorial *= i
        print(i)
    print(factorial)
#  Finding factorial with recursive function.
def find_factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * find_factorial_recursive(n-1)

find_factorial(8)
print(find_factorial_recursive(8))

# ! Question 3
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
def find_square(n):
    squares = {}
    for i in range(1,n+ 1):
        squares[i] = i**2
    return squares
print(find_square(8))


# ! Question 4
def tuple_and_list_generator():
    pass


nums_tuple = ()
nums_list = []
# raw_num = input('Enter numbers: ')
# numberss = list(map(int, raw_num.split(',')))
nums_list = list(map(int,input("Enter numbers: ").split(",")))
nums_tuple = tuple(nums_list)
print(nums_list,nums_tuple)
class Foo:
    def test(self):
        print("This is test method")
    def get_string(self,str):
        print(str)
f = Foo()
f.test()
f.get_string("manzoor Hussain")