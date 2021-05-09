# 74. Write a Python program to pack consecutive duplicates of a given list elements into sublists. Go to the editor
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After packing consecutive duplicates of the said list elements into sublists:
# [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
# def pack_consective(list):
#     new_list = []
#     for i in range(len(list)):
#         print(list.count(list[i]))
#         if list.count(list[i])>1:
#             new_list.extend((list[i])*(list.count(list[i])))
from itertools import groupby
def pack_consective(lst):
    new_list = []
    new_list2 = []
    for key, group in groupby(lst):
        new_list2.append(list(group))
        # print(list(group))
    new_list = [list(group) for key, group in groupby(lst)]
        # print(list(group))
    print(new_list)
    print(new_list2)

lst = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
pack_consective(lst)
