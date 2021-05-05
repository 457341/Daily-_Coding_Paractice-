# Here I am going to write the some programs with different types of for loops in Python.
for i in range(5):# default starting position is zero(0), and the last point in not exlusive. increment is 1 by default
    print(i)
print('................................................................')
for i in range(1,5):# here stating point is 1 , increment is 1 by default
    print(i)


print('................................................................')
for i in range(1,5,2):# increment is 2 
    print(i)

print('................................................................')
for i in range(1,5):
    print(i)
    i += 2 # increment is not working in this way