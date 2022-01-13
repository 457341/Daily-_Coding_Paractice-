
square = lambda x : x*x
cube = lambda x : x*x*x
print(square(2))
print(cube(2))

# 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result. Go to the editor
# Sample Output:
# 25
# 48
l = lambda x : x+15 # Addition
print(l(4))
l2 = lambda x ,y : x * y # Multiplication
print(l2(2,3))

# 2. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number. Go to the editor
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75

def foo(n):
    return lambda x:x*n
result = foo(2)(10)
print(result)
#? Also Can be called as below:
result = foo(3)
print(result(15))
# Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:c
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

lst = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_list = sorted(lst, key=lambda x: x[1])
print (sorted_list)
lst.sort(key = lambda x: x[1])
print(lst)

# Write a Python program to sort a list of dictionaries using Lambda. Go to the editor
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

dic = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
dic.sort(key=lambda x: x['color'])
print(dic)

print("*"*100,'\n')
# 5. Write a Python program to filter a list of integers using Lambda. Go to the editor
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]
int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filter(function, iterable), iterable - an iterable like sets, lists, tuples etc.
even_list = filter(lambda x: x %2 == 0, int_list)
print(even_list)
even_list = list(even_list)
print(even_list)

odd_list = list(filter(lambda x: x % 2 != 0, int_list))
print("Odd numbers: ",odd_list)

# 6. Write a Python program to square and cube every number in a given list of integers using Lambda. Go to the editor
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_lst = list(map(lambda x:x*x,lst))
print("Square List",square_lst)
cubic_lst = list(map(lambda x:x*x*x,lst))
print("Cubic List",cubic_lst)

starts_with = lambda x: True if x.startswith('P') else False
print(starts_with("Python"))
print(starts_with("Java"))

# . Write a Python program to extract year, month, date and time using Lambda. Go to the editor
# Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178
import datetime
now = datetime.datetime.now()
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
timee = lambda x: x.time
print(year(now))
print(month(now))
print(day(now))
print(timee(now))

# Write a Python program to create Fibonacci series upto n using Lambda.
from functools import reduce

fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                range(n-2), [0, 1])

print("Fibonacci series upto 2:")
print(fib_series(2))
print("\nFibonacci series upto 5:")
print(fib_series(5))
print("\nFibonacci series upto 6:")
print(fib_series(6))
print("\nFibonacci series upto 9:")
print(fib_series(9))
# Write a Python program to find intersection of two given arrays using Lambda.
array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]
print("Original arrays:")
print(array_nums1)
print(array_nums2)
result = list(filter(lambda x: x in array_nums1, array_nums2)) 
print ("\nIntersection of the said arrays: ",result)

# Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
print("Original arrays:")
print(array_nums)
result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)
print("\nRearrange positive and negative numbers of the said array:")

# Write a Python program to find numbers within a given range where every number is divisible by every digit it contains.
def divisible_by_digits(start_num, end_num):
    return [n for n in range(start_num, end_num+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
print(divisible_by_digits(1,22))

# Find palindromes in a given list of strings using Lambda
texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
print("Orginal list of strings:")
print(texts) 
result = list(filter(lambda x: (x == "".join(reversed(x))), texts)) 
print("\nList of palindromes:")
print(result) 


my_list = [21,13,19,3,11,5,18]
my_list.sort()
print(my_list)
print(my_list[len(my_list)//2])
print(list(range(10,1,-1)))
print(list(reversed(range(1,10))))
print(reversed(list(range(1,11))))
print(list(reversed(range(1,11))))

# Write a Python program to find the numbers of a given string and store them in a list, display the numbers which are bigger than the length of the list in sorted form. Use lambda function to solve the problem.

str1 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
print("Original string: ",str1)
str_num=[i for i in str1.split(' ')]
lenght=len(str_num)
numbers=sorted([int(x) for x in str_num if x.isdigit()])
print('Numbers in sorted form:')
for i in ((filter(lambda x:x>lenght,numbers))):
    print(i,end=' ')

# Write a Python program that multiply each number of given list with a given number using lambda function. Print the result.
nums = [2, 4, 6, 9 , 11]
n = 2
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print(' '.join(map(str,filtered_numbers)))

# Write a Python program to find the list with maximum and minimum length using lambda.
def max_length_list(input_list):
    max_length = max(len(x) for x in input_list )   
    max_list = max(input_list, key = lambda i: len(i))    
    return(max_length, max_list)
    
def min_length_list(input_list):
    min_length = min(len(x) for x in input_list )  
    min_list = min(input_list, key = lambda i: len(i))
    return(min_length, min_list)
      
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
print("Original list:")
print(list1)
print("\nList with maximum length of lists:")
print(max_length_list(list1))
print("\nList with minimum length of lists:")
print(min_length_list(list1))

# Write a Python program to remove all elements from a given list present in another list using lambda.
def index_on_inner_list(list1, list2):
    result = list(filter(lambda x: x not in list2, list1))
    return result
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8]
print("Original lists:")
print("list1:", list1)
print("list2:", list2)
print("\nRemove all elements from 'list1' present in 'list2:")
print(index_on_inner_list(list1, list2))

# Write a Python program to convert string element to integer inside a given tuple using lambda.


def tuple_int_str(tuple_str):
    result = tuple(map(lambda x: (int(x[0]), int(x[2])), tuple_str))
    return result     
tuple_str =  (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
print("Original tuple values:")
print(tuple_str)
print("\nNew tuple values:")
print(tuple_int_str(tuple_str))


# Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings.
def sort_mixed_list(mixed_list):
    mixed_list.sort(key=lambda e: (isinstance(e, str), e))
    return mixed_list
mixed_list = [19,'red',12,'green','blue', 10,'white','green',1]
print("Original list:")
print(mixed_list)
print("Sort the said  mixed list of integers and strings:")
print(sort_mixed_list(mixed_list))


def max_min_list_tuples(class_students):
    return_max = max(class_students,key=lambda item:item[1])[1]
    return_min = min(class_students,key=lambda item:item[1])[1]
    return return_max, return_min
    

# Write a Python program to find the maximum and minimum values in a given list of tuples using lambda function.


class_students = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
print("Original list with tuples:")
print(class_students)
print("\nMaximum and minimum values of the said list of tuples:")
print(max_min_list_tuples(class_students))
print(max_min_list_tuples(class_students))

def max_min_list_tupless(class_students):
    return_max = max(class_students,key=lambda item:item[1])[1]
    return_min = min(class_students,key=lambda item:item[1])[1]
    return return_max, return_min