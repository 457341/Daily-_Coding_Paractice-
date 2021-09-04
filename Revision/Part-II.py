# ? Question
# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
# ! Answer
# def foo(data):
#     if len(data) == len(set(data)):
#         return True
#     else:
#         return False
# print(foo([1,2,3]))
# print(foo([1,1,3, 4, 5, 6, 7]))
#? Question
# Write a Python program to count the number of each character of a given text of a text file.
f = open("text.txt", "r")
# print(f.read())
str = "My name is manzoor"
str = str.split()
for s in str:
    s = s.split()
    print(s)
print(str)
#! Answer

def remove_nums(int_list):
  #list starts with 0 index
  position = 3 - 1 
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    idx = (position+idx)%len_list
    print(int_list.pop(idx))
    len_list -= 1
nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)
