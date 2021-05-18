# 102. Write a Python program to extract specified size of strings from a give list of string values. 
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# length of the string to extract:
# 8
# After extracting strings of specified length from the said list:
# ['practice', 'solution']

def extract_specified_size(list,size):
    new_list = []
    for key,value in enumerate(list):
        if len(value) == size:
            new_list.append(value)
    print(new_list)
list = ['Python', 'list', 'exercises', 'practice', 'solution']
extract_specified_size(list,8)


    