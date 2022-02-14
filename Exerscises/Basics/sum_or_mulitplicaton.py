# Given two integer numbers return their product only if the product is greater than 1000, else return their sum.


def sum_or_mulitplicaton(num1,num2):
    product = num1 *num2

    if product >=1000:
        return product
    else:
        return num1 + num2

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
print("Result: ",sum_or_mulitplicaton(num1,num2))