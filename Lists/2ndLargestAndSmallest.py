# Write a Python program to find the second smallest number in a list. Go to the editor
# Click me to see the sample solution
import random

def second_largest_number(list):
    print(f'original list: {list}')

    list = sorted(list)
    print(f'sorted list: {list}')
    print(f'Second largest number: {list[-2]}')

# 28. Write a Python program to find the second largest number in a list. Go to the editor
# Click me to see the sample solution
def second_smallest_number(list):
    print(f'original list: {list}')
    list = sorted(list)
    print(f'sorted list: {list}')
    print(f'Second smallest number: {list[1]}')

def generate_random_num_list():
    random_list = []
    for i in range(0,6):
        random_list.append(random.randint(0,30))
    return random_list
  


second_largest_number(generate_random_num_list())
second_smallest_number(generate_random_num_list())

