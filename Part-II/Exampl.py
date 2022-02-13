# Write a Python program to create a coded string from a given string, using specified formula.

# Replace all 'P' with '9', 'T' with '0', 'S' with '1', 'H' with '6' and 'A' with '8'

def test(str):
	return str.translate(str.maketrans('PTSHA', '90168'))
str = "PHP"
print("Original string: ",str)
print("Coded string: ",test(str))
str = "JAVASCRIPT"
print("\nOriginal string: ",str)
print("Coded string: ",test(str))
print("Coded string: ",test(str))



from datetime import date
print("Input month and date (separated by a single space):")
m, d = map(int, input().split())
weeks = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
w = date.isoweekday(date(2016, m, d))
print("Name of the date: ",weeks[w])
