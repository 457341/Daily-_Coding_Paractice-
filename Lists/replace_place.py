# Write a Python program to change the position of every n-th value with the (n+1)th in a list. 
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
def replace_place(list):
    print(list)
    i = 0
    while i < len(list):
        temp = list[i]
        list[i] = list[i+1]
        list[i+1] = temp
        i = i + 2
    print(list)

list = [0, 1, 2, 3, 4, 5]
replace_place(list)