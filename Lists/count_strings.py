# Write a Python program to count the number of strings where the string length is 2 or more and the 
# first and last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def count_string(list):
    count = 0
    for i in list:
        if len(i) >2 and  i[0] == i[-1]:
            count += 1
    print(count)
lst = ['abc', 'xyz', 'aba', '1221']
count_string(lst)


