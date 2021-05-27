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