# declaring set
set_declaration = set()
print(set_declaration)
print(type(set_declaration))

# iterating over set
name = set("Manzoor")
for val in name:
    print(val,end='') # There is no proper sequece here, sometimes print azorMn,sometime oaMrnz
print('')
# adding the numbers 
numbers = set([1,2,3,4,5]) # if there is duplicates, they will be ignored.
count = 0
numbers.add(10) # Adding element to numbers
numbers.pop() # at index 0 the number will be deleted.
for i in numbers:
    count = count + i
print(count)
print(numbers)
num1 = {1,2,3,4,5}
num2 = {4,5,6,7,9}
num_unions = num1.union(num2)
num_intersections = num1.intersection(num2)
num1_difference = num1.difference(num2) # Elements of num1 which are not available in num2.
num2_difference = num2.difference(num1)# Elements of num2 which are not available in num1.
print("Union: ",num_unions)
print("Intersection: ",num_intersections)
print("Num1 Difference: ",num1_difference)
print("Num2 Difference: ",num2_difference)


# Symetric Difference
A = {1,2,3}
B = {1,2,4}
subset_difference = A ^ B
print("Subset Difference: ",subset_difference)

# second lecture
# checking subset
setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])
print(setx.issubset(sety))
print(setx.issubset(setz))
print(setz.issubset(sety))
print(setz.issubset(setx))

# copyings the set
set_of_numbers = {1,2,3,4,5}
set_numbers = set_of_numbers.copy()
print("Copy: ",set_numbers)

# Removing all elements from set
set_of_numbers.clear()
print("Deleted: ",set_of_numbers)
# find max and min value in a set
max_value = 0
min_value = 5
for i in set_numbers:
    if i > max_value:
        max_value = i
    if i < min_value:
        min_value = i
print(f'Max value: {max_value} and min value: {min_value}')
print(max(set_numbers)) # With Function
print(min(set_numbers)) # With Function
# find length of a set
print("Length of a set is: ",len(set_numbers))
# Check if two set has  elements not in common
set_a = {1,2,3}
set_b = {1,3}
set_c = {4}
print(set_a.isdisjoint(set_b))
print(set_b.isdisjoint(set_a))
print(set_c.isdisjoint(set_a))
# check if value is present in set or not
print(3 in set_a)

