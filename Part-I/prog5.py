# 5. Write a Python program which accepts the user's first and last name 
# and print them in reverse order with a space between them. 
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")


first_name_reversed  = []
last_name_reversed  = []
C:\Users\husey\OneDrive\Desktop\8th semester\Python (Don't break the chain)\prog5.py


j = len(first_name) -1 # Length of first name
k = len(last_name) - 1 # Length of last name
for i in first_name:

    first_name_reversed.append(first_name[j]) 
    j -=1

for i in last_name:
    last_name_reversed.append(last_name[k])
    k -= 1

first_name = ''.join(map(str, first_name_reversed)) 
last_name = ''.join(map(str, last_name_reversed)) 
print(first_name," ",last_name)