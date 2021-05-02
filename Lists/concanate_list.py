#  Write a Python program to create a list by concatenating a given list which range goes from 1 to n. Go to the editor
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

import random
def concanate_list(list,size):
    print('')
    news_list = []
    first = list[0]
    second = list[1]
    for i in range(1,size+1):
        news_list.append(first+str(i))
        news_list.append(second+str(i))
    print(news_list)

list = ['p','q']
size = random.randint(0,6) # Random size number generator
concanate_list(list,size)