# Write a Python program to insert a given string at the beginning of all items in a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
def insert(list,string):
    for i in range(len(list)):
        list[i] = string +str(list[i])
    print(list)
list,string = [1,2,3,4,5],"emp"
insert(list,string)

num = [1,2,3,4]
print(['emp{}'.format(i) for i in  num])