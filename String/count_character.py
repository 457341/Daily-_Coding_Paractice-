# Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
simple_string = input("Enter string: ")
string_dic = {}
for i in simple_string:
    string_dic[i] = simple_string.count(i)
print(string_dic)