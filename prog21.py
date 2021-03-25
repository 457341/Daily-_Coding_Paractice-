# Write a Python program to create a histogram from a given list of integers

histList = [2,3,6,5]
def drawHistagram(lst):
    strr = ''
    for i in lst:
        strr = strr + ('*') * i + '\n'
    return strr
print(drawHistagram(histList))
print(drawHistagram([10,9,8,7,6,5,4,3,2,1]))