# Write a Python program to check if a nested list is a subset of another nested list.
def check_subset(list,subset):
    return any(map(list.__contains__, subset)) # for any one
    # return all(map(list.__contains__, subset)) # for all


list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]] 
list2 = [[1, 2],[13,15,17]] 
print(check_subset(list1,list2))

#! Question2: Write a Python program to count the number of sublists contain a particular element
def count_number(lst,element):
    count = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            # print(lst[i])
            if lst[i][j] == element:
                count += 1
        # print("manzoor")
    print("Total count of ",element,"is: ",count)
list3 = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# count_number(list3,1)
# count_number(list3,7)

list4 = [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
# count_number(list4,"A")

def count_number2(lst,element):
    # count = 
    
    return len(([lst[i][j]  for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == element ]))
list3 = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# print(count_number2(list3,1))

def count_number3(lst,element):
    count = 0
    toplam = 0
    for index,value in enumerate(lst):
        # print(index,value)
        for v in value:
            # print(v)
            if v == element:
                count = count + 1
    toplam = len([v for index,value in enumerate(lst) for v in value if v == element])
    print("Total count of ",element,"is: ",count)
    print("Total count of ",element,"is: ",toplam)
def count_number4(lst,element):
    count = 0
    for i in range(len(lst)):
        if element in lst[i]:
            count += 1
    print("Total count of ",element,"is: ",count)
count_number3(list3,7)
count_number4(list3,7)