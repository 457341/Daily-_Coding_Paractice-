# 51. Write a Python program to split a list every Nth element. 
# Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

def split_nth(list,n):
    double_list = []
    for i in range(n):
        # print(i)

        # print(list[i::n])
        double_list.append(list[i::n])
    print(double_list)

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
split_nth(list,3)
