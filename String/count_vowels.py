# 49.Write a Python program to count and display the vowels of a given text
def countVowels(string):
    count_vowlels = {}
    count = 0
    for i in string:
        if i  == 'a' or i == 'e' or i ==  'i' or   i =='o' or i== 'u':
            count = count + 1
    print(count)

countVowels("manzoor")

# ! Solution 2
def count_vowlels2(string):
    vowels = "aeiouAEIOU"
    print(len([i for i in string if i in vowels]))
    print([i for i in string if i in vowels])
count_vowlels2("manzoor")
