
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
square_list = list(map(lambda x:x*x,lst))
print("Square List:",square_list)
cubic_list = list(map(lambda x:x*x*x,lst))
print("Cubic List:",cubic_list)
