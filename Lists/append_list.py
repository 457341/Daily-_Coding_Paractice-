# Write a Python program to append a list to the second list
def append_list(list1,list2):
    print("")
    print("")

    # list1.append(list2)
    # print(list1)
    for i in list2:
        list1.append(i)
    print(list1)
list1 = [1,2,3,4,5]
list2 = [6,7,8,9]
# append_list(list1,list2)


# another solution is below:
print(list1+list2)