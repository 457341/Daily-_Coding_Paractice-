with open('test.txt','a') as f:
    f.write("Hussain")
    # print(f.read())

with open('test.txt','r') as f:
    print(f.read())
# Reading and writing(copying) to another file
with open('manzoor.txt','r') as rf:
    for line in rf:
        with open('test.txt','a') as wf:
            wf.write(line)
with open('manzoor.txt','r') as rf:
    with open('test.txt','a') as wf:
        for line in rf:
            wf.write(line)
with open('test.txt','r') as f:
    print(f.read())