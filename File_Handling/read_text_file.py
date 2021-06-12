# There are tow ways to read a file and
#! Way1: with open file, in this method we have to close the file explicitly
f = open('manzoor.txt')
print(f.read())
print(f.mode)
print(f.closed)
f.close()
print(f.closed)
#! In this method file will be closed automatically. This is called context manager.#
with open('manzoor.txt') as file:
    print(file.read())
    print(f.name) # printing the name of file

print(file.closed)# True
#print(file.read())# Will get an error.

with open('manzoor.txt') as file:
    # print(file.readlines())
    # upper line prints : ['My name is Manzoor Hussain. Line One\n', 'I am from Pakistan. Line Two\n', 'I live in Turkey. Line Three']
    #? Best practice to read entire file. In this way there is no memory issue.
    for line in file:
        print(line,end='')

with open('manzoor.txt') as f:
    print(f.read(10),end='--') # We can mention the size. Here read() will read 10 characters
    print(f.read(10),end='--') # We can mention the size. Here read() will read 10 characters
    print(f.read(10),end='--') # We can mention the size. Here read() will read 10 characters
with open('manzoor.txt') as f:
    # For better usability we should mention the size. To read full file we have to write below code.
    read_size = 10
    content = f.read(read_size)
    while len(content) > 0:
        print(content,end='\n*')
        print(f.tell()) # Shows the current position 
        f.seek(0) # changing the position
        content = f.read(read_size)
        