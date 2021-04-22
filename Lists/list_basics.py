# Write a Python program to sum all the items in a list
def sum(list):
    sum = 0
    for i in list:
        sum = sum+i

    print(sum)

# sum(['m','a','n','z','o','o','r'])
# sum([1,2,3])

# Write a Python program to multiplies all the items in a list
def multiply(list):
    mul = 1
    for i in list:
        mul = mul*i

    print(mul)

# sum(['m','a','n','z','o','o','r'])


# Write a Python program to get the largest number from a list. 
# Click me to see the sample solution


def laraget(list):
    laraget = list[0]
    for i in list:
        if i>laraget:
            laraget = i
    print("largest number is: ",laraget)


#  Write a Python program to get the smallest number from a list. 
# Click me to see the sample solution

def smallest(list):
    smallest = list[0]
    for i in list:
        if i<smallest:
            smallest = i
    print("largest number is: ",smallest)












sum([1,2,3])
multiply([1,3,3])
laraget([1,7,3])
smallest([1,7,3])

