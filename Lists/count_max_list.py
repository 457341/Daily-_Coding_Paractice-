# 91. Write a Python program to find the list with maximum and minimum length. Go to the editor
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
# List with maximum length of lists:
# (3, [3, 5, 7])
# List with minimum length of lists:
# (1, [0])
# Original list:
# [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
# List with maximum length of lists:
# (4, [1, 34, 5, 7])
# List with minimum length of lists:
# (1, [12])
def count_max_list(list):
    min_length = 1
    max_length = 1
    new_max_list = []
    new_min_list = []
    for key,value in enumerate(list):
        if len(value)>max_length:
            max_length = len(value)
            new_max_list = value
        if len(value)<min_length:
            min_length = len(value)
            new_min_list = value

    # return [value for key,value in enumerate(list) if max(len(value))]
    print("Max length and list",max_length,new_max_list)
    print("min length and list",min_length,new_min_list)
    # print(max(len(list)))
list1 =[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# count_max_list(list1)

# very simple solutions
def max_length_list(list):
    max_length = max((len(x) for x in list))
    max_list = max(list,key = len)
    return (max_length,max_list)
def min_length_list(list):
    min_length = min((len(x) for x in list))
    min_list = min(list,key = len)
    return (min_length,min_list)



print(max_length_list(list1))
print(min_length_list(list1))
# count_max_list(list)
# count_max_list(list)
# count_max_list(list)