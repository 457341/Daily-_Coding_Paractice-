# Write a Python program to count integer in a given mixed list. Go to the editor
# Original list:
# [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# Number of integers in the said mixed list:
# 6
def count_integer(list):
    count = 0
    count = len([j for i,j in enumerate(list) if isinstance(j, int)])
    # print(new_list)
    print(count)
lst = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
count_integer(lst)

#! Question2: 
# Write a Python program to remove a specified column from a given nested list. Go to the editor
# Original Nested list:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# After removing 1st column:
# [[2, 3], [4, 5], [1, 1]]
# Original Nested list:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# After removing 3rd column:
# [[1, 2], [-2, 4], [1, -1]]
def remove_column(lst,n):
    for i in lst:
        # del lst[n] # it removes all columns other than lst[n]
        del i[n]

    print(lst)
remove_column([[1, 2, 3], [2, 4, 5], [1, 1, 1]],1)

#! Question3: 
# Write a Python program to extract a specified column from a given nested list. Go to the editor
# Original Nested list:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Extract 1st column:
# [1, 2, 1]
# Original Nested list:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Extract 3rd column:
# [3, -5, 1]

def extract_column(lst,n):
    new_list = [i.pop(n) for i in lst]
    print(new_list)
extract_column([[1, 2, 3], [2, 4, 5], [1, 1, 1]],0)
extract_column([[1, 2, 3], [-2, 4, -5], [1, -1, 1]],2)

