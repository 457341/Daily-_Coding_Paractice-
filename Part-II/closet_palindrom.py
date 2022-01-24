def test(n):
    x = n
    y = n
    while True:
        if str(x) == str(x)[::-1]:
            return x
        x -=  1
        if str(y) == str(y)[::-1]:
            return y
        y += 1
    return int(bin(n)[::-1][:-2], 2)

n = 120;
print("Original number: ", n);
print("Closest Palindrome number of the said number: ",test(n));
n = 321;
print("Original number: ", n);
print("Closest Palindrome number of the said number: ",test(n));
n = 43;
print("Original number: ", n);
print("Closest Palindrome number of the said number: ",test(n));
n = 1234;
print("Original number: ", n);
print("Closest Palindrome number of the said number: ",test(n));
