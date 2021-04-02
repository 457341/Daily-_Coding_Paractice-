#  Write a Python program to get a new string from a given string where "Is" 
#  has been added to the front. If the given string already
#   begins with "Is" then return the string unchanged

given_string = (input("Enter the string: "))
if given_string.startswith("Is"):
    print(given_string)
else:
    print("Is "+given_string)

# Write a Python program to find whether a given number (accept from the user) is even or odd,
#  print out an appropriate message to the user

number = int(input("Enter number: "))
if number %2 == 0:
    print(number," is an even number.")
else:
    print(number," is an odd number.")
    

#  Write a Python program to count the number 4 in a given list.
lst = [4,4,5,6,7,1,2,14]
total_4 = lst.count(4)
print("There is total: ",total_4 ," values of 4")


# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. 
# Return the n copies of the whole string if the length is less than 2
def fun(str,n):
    first_two_chracter = str[0:2]
    first_two_chracter = first_two_chracter*n
    if len(str) <2:
        str = str *n
        return str
    return first_two_chracter
print(fun("Manzoor",3))
print(fun("M",10))
# Write a Python program to test whether a passed letter is a vowel or not
# alphabet = input("Enter alphabet: ")
# alphabet = 'b'
# isVowel = alphabet == 'a' or alphabet == 'e'or alphabet == 'i' or alphabet == 'o' or alphabet == 'u'
# if isVowel == True:
#     print(alphabet," is a vowel")
# if isVowel == False:
#     print(alphabet," is not a vowel")
def vowelOrNot(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(vowelOrNot('z'))
print(vowelOrNot('o'))