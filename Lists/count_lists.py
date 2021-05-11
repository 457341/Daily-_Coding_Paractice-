# 90. Write a Python program to count number of lists in a given list of lists. Go to the editor
# Original list:
# [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# Number of lists in said list of lists:
# 4
# Original list:
# [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
# Number of lists in said list of lists:
# 3

def count_lists(list):
    count = 0
    for key,value in enumerate(list):
        print("key: ",key,"value: ",value)
        count += 1
    
    print("count: ",count)
list = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
list2 = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
count_lists(list)
count_lists(list2)
# very simple way
print("count",len(list))
print("count",len(list2))