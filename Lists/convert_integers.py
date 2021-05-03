# Write a Python program to convert a list of multiple integers into a single integer
def convert_int(list):
    oneInteger = ''
    for i in list:
        oneInteger += str(i)
    print(oneInteger)

convert_int([11,20,30,40,])