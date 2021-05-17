# Write a Python program to sort a given matrix in ascending order according to the sum of its rows. Go to the editor
# Original Matrix:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
# Original Matrix:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
# def sort_matrix(lst):
    # for i in range(len(lst)):
    #     print(i)
    # for key,value in enumerate(lst):
    #     value.sort(key=sum(value))
    #     print(value)
    # print("After sorting",lst)
l1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
l2 = [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
print("Original",l2)
# sort_matrix(l1)
l2.sort()
print("after sorting",l2)