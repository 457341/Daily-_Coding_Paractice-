# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
def generate_array(row,column):
    array = []
    array = [[0 for c in range(column)] for r in range(row)] # Here we are initializing array. Any value we can put initially
    # array = [[1 for c in range(column)] for r in range(row)]
    for i in range(row):
        for j in range(column):
            # array[i][j].append(i*j) = i*j
            # array.append(i*j)
            # array[i][j] = i*j
            # array[i][j] = i*j
            array[i][j] = i*j 
    # array = [i*j for i in range(column) for j in range(row) ]
    return array
row,column = input("Enter rows and colums: ").split()
row = int(row)
column = int(column)
# print(row+column)
print(generate_array(row,column))