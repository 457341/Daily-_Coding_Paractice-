# Write a Python function that takes a sequence of numbers and determines whether 
# all the numbers are different from each other.

def distinct_test(list):
    if len(set(list)) == (len(list)):
        print("All elements are different")
    else:
        print("There is duplicate values available.")
    
distinct_test([1,2,3,1,4])
distinct_test([1,3,6,7,9,0])
distinct_test(['a','b'])