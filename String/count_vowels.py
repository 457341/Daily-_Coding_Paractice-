# 49.Write a Python program to count and display the vowels of a given text
def countVowels(string):
    count_vowlels = {}
    count = 0
    for i in string:
        if i  == 'a' or i == 'e' or i ==  'i' or   i =='o' or i== 'u':
            count = count + 1
    print(count)

countVowels("manzoor")