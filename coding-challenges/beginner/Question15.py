# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
def compute_number(n):
    num = n + int(str(n)*2) + int(str(n)*3) + int(str(n)*4)
    print(num)
number = 9
compute_number(number)
