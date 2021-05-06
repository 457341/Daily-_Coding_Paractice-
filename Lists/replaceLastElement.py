# Write a Python program to replace the last element in a list with another list
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
def replace_last_element(list1,list2):
    list1[-1:] = list2
    print(list1)

list1,list2 = [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
replace_last_element(list1,list2)