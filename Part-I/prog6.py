#6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate
#  a list and a tuple with those numbers. 
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')
lst = [];lst2 = []
tple = (); tple2 = ()

# method 1
lst = [int(i) for i in input("Enter Numbers: ").split(",")]
tple = tuple(lst)
print(lst)
print(tple)

# Method 2
lst2 = list(map(int,input("Enter Numbers: ").split(",")))
tple2 = tuple(lst2)
print(lst2)
print(tple2)