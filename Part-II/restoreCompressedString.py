# When character are consecutive in a string , it is possible to shorten the character string by replacing 
# the character with a certain rule. For example, in the case of the character string YYYYY, if it is 
# expressed as # 5 Y, it is compressed by one character.
# Write a Python program to restore the original string by entering the compressed string with this rule. However,
#  the # character does not appear in the restored character string. Go to the editor
# Note: The original sentences are uppercase letters, lowercase letters, numbers, symbols, less than 100 letters,
#  and consecutive letters are not more than 9 letters.
# Input:
# The restored character string for each character on one line.
# Original text: XY#6Z1#4023
# XYZZZZZZ1000023
# Original text: #39+1=1#30
# 999+1=1000


str = input("Enter String: ")
# print(str)
def restore_string(str):
    compressed_string = []
    for i in str:
        # print(i)
        compressed_string.append(i)
        j = 0
    for i in compressed_string:
        if i == '#':
            compressed_string[j] = ''
            compressed_string[j+1] = compressed_string[j+2]*(int(compressed_string[j+1]  ) -1)
        j += 1
    listToStr = ' '.join([str(elem) for elem in compressed_string]) 
    print(compressed_string)
    print(listToStr)
restore_string(str)
