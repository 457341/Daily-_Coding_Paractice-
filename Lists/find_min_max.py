def find_odd_values(min_value, max_value):
    odd_values =[]
    odd_values = [i for i in range(min_value, max_value +1) if i %2 == 1] # putting odd numbers into odd_values
    return odd_values
min_max_values = input("Enter min max values: ").split() # spliting input based on space
min_value = int(min_max_values[0]) # type casting from string to int
max_value = int(min_max_values[1]) # type casting from string to int
print(find_odd_values(min_value,max_value))