# Exercise 3: Print characters from a string that are present at an even index number



string = input("Enter String: ")
# for i in string:
#     print(i)
#     i = i + 2
# for index,value in enumerate(string):
#     print("Index: ",index,"value",value)
#     index = index + 2
for i in range(0,len(string),2):
    print("index: ",i,"value: ",string[i])
    # i = i + 2