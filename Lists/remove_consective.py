# 73. Write a Python program to remove consecutive duplicates of a given list.
from itertools import groupby
#     # print(new_list)

def remove_duplicate(list):
    new_list = []
    # print(len(list))
    for i in range(len(list)+2):
        if  i<len(list)-1 :
            if list[i] == list[i+1]:
                continue
            else:
                new_list.append(list[i])

    print(new_list)#[0, 4, 6, 6, 4]

def removeDuplicate(list):
    new_list = []
    for key,group in groupby(list):
        new_list.append(key)
    print(new_list)

list =[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
list2 = ['a','a','b','b','c','c','d','d','e','e','f','g','h']
# remove_duplicate(list)
removeDuplicate(list)
removeDuplicate(list2)
        
