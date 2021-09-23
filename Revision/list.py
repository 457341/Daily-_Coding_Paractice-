#? Question 
# 1. Write a Python program to sum all the items in a list. 
#! Answer 
lst = [1, 2, 3, 4, 5, 6]
print("Sum of list is: ",sum(lst))

#? Question 
# 2. Write a Python program to multiply all the items in a list. 
#! Answer 
def multiply(lst):
    mul = 1
    for i in lst:
        mul *= i
    return mul
print("Multiplication of list is: ",multiply(lst))

#? Question 
# 3. Write a Python program to get the largest number from a list. 
#! Answer 
def largest(lst):
    largest_number = 1
    for i in lst:
        if largest_number < i:
            largest_number = i
    return largest_number
print("Largest number in list is: ",largest(lst))
#? Question 
# 4. Write a Python program to get the smallest number from a list. 
#! Answer 
def smallest(lst):
    smallest_number = lst[0]
    for i in lst:
        if smallest_number > i:
            smallest_number = i
    return smallest_number

print("The smallest number in list is: ",smallest(lst))
#? Question 
# 5. Write a Python program to count the number of strings where the string length is 2 or more 
# and the first and last character are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

#! Answer 
def check_first_and_last_characters(lst):
    total = 0
    if len(lst) >= 2:
        for i in lst:
            if i[0] == i[-1]:
                total += 1
    return total

result = check_first_and_last_characters( ['abc', 'xyx', 'aba', '1221'])
print("The result is: " ,result)
# sonuc = 0
# result2 = [sonuc +=1 :if if i[0] == i[-1]]
#? Question
# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
#! Answer
def last_element(n):
    return  n[-1] # Here n[1] is also fine
def Question_6(lst):
    # for index,i in enumerate(list):
    #     print(i)
    #     print(sum(i))
    #     print(i[0])
    return sorted(lst,key=last_element)
q6_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("List before sorting(according to the last element of list): ",q6_list)
print("List after sorting(according to the last element of list): ",Question_6(q6_list))

# print(Question_6([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
# def last(n): return n[-1]
# def sort_list_last(tuples):
#   return sorted(tuples, key=last)

# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

#? Question
# 7. Write a Python program to remove duplicates from a list. 
# def Question_7()
#? Question
# 8. Write a Python program to check a list is empty or not. 

#! Answer
#? Question
# 9. Write a Python program to clone or copy a list. 

#! Answer
#? Question
# 10. Write a Python program to find the list of words that are longer than n from a given list of words. 

#! Answer
#? Question
# 11. Write a Python function that takes two lists and returns True if they have at least one common member. 
#! Answer

#? Question
#! Answer
# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']