# Write a Python program to convert a list of characters into a string
def convert_to_string(list):
    print(''.join(list))
convert_to_string(['m','a','n','z','o','o','r'])

# Write a Python program to find the index of an item in a specified list
def foo(list):
    for key,value in enumerate(list):
        print(key,value)
foo(['h','u','s','a','i','n'])