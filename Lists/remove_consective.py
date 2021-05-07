# 73. Write a Python program to remove consecutive duplicates of a given list.
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After removing consecutive duplicates:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

def remove_duplicate(list):
    new_list = []
    j = 0
    for i in range(len(list)):
        if list[j] == list[j+1]:
            print(list[j])
            # new_list.append(list[i])
            j += 1
            
    # print(new_list)



list =[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
remove_duplicate(list)
        
