


# Write a Python program to concatenate all elements in a list into a string and return it.
# lst = ['m','a','n','z','o','o','r']
# str = ''
# for i in lst:
#     str = str + i
def concat_elements(lst):
    str2 = ''
    for i in lst:
        str2 = str2 + str(i)
    return str2
print(concat_elements([1,2,3,4]))
# print(str)