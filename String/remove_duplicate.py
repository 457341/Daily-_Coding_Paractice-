#  Write a Python program to remove duplicate characters of a given string
def remove_dulicate(string):
    non_duplicated =[]
    string = list(string)
    for i in string:
        if string.count(i) ==1:
            non_duplicated.append(i)
    non_duplicated = ''.join(non_duplicated)
    print("Non duplicated: ",non_duplicated)
remove_dulicate("manzoor hussain")# mnzrhui