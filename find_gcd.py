#Write a Python program to compute the greatest common divisor (GCD) of two positive integers
# def findGCD(num1,num2):
#     greatest = 1
#     smallNum = 1
#     if num1 > num2:
#         smallNum = num2
#     elif num1 < num2 or num1 == num2:
#         smallNum = num1
#     for i in range(1,smallNum):
#         if num1 % i == 0 & num2 % i == 0:
#             greatest = i
        
#     return greatest

# print("The greatest number is: ",findGCD(24,60))
# print("The greatest number is: ",findGCD(15,20))
# print("The greatest number is: ",findGCD(100,75))
# resultList = []
# num = 60
# # while num >=1:
# for i in range(2,num+1):
#     # if num == 1:
#     #     break
#     if num % i == 0:
#         res = num/i
#         j = i
#         num = res 
#         i = j
#         resultList.append(i)
# print("this is working")
# print(resultList)
# lst1 = set([2,3,4])
# lst2 = set([2,4])
# lst3 = lst1.difference(lst2)
# print(lst3)
# print(lst1.intersection(lst2))

def make_list(num):
    lst = []
    for i in range(2,num):
        if num % i == 0:
            lst.append(i)
    return lst
def find_gcd(num1,num2):
    lst1 = set(make_list(num1))
    lst2 = set(make_list(num2)) 
    lst3 = lst1.intersection(lst2)
    maks = max(lst3, default=1)
    print("The greatest diviser is: ",maks)

find_gcd(24,60)
find_gcd(60,24)
find_gcd(12, 17)
find_gcd(4, 6)
find_gcd(100,75)
find_gcd(112,46)
find_gcd(55,33)