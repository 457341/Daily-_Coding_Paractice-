# There are tow ways to read a file and
#! Way1: with open file, in this method we have to close the file explicitly
f = open('manzoor.txt')
print(f.read())
print(f.mode)
print(f.closed)
f.close()
print(f.closed)
#! In this method file will be closed automatically.
with open('manzoor.txt') as file:
    print(file.read())

print(file.closed)# True
print(file.read())# Will get an error.