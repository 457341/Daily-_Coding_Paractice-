# 103. Write a Python program to extract specified number of elements from a given list, which follows each other continuously. Go to the editor
# Original list:
# [1, 1, 3, 4, 4, 5, 6, 7]
# Extract 2 number of elements from the said list which follows each other continuously:
# [1, 4]
# Original lists:
# [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
# Extract 4 number of elements from the said list which follows each other continuously:
# [4]
from itertools import groupby
def extract_specified_number(lst,size):
    new_list = [i for i,j in groupby(lst) if len(list(j)) == size]
    # for i,j in groupby(list):
    #     print(i,tuple(j))
    print(new_list)
list1 = [1, 1, 3, 4, 4, 5, 6, 7]
extract_specified_number(list1,2)
list2 = [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
extract_specified_number(list2,4)