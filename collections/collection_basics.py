# Write a Python program that iterate over elements repeating each as many times as its count.

from collections import Counter
c = Counter(p=4, q=2, r=0, s=-2)
d = Counter(d =4)
print(list(c.elements()))
print(tuple(d.elements()))
# Write a Python program to find the most common elements and their counts of a specified text.
name = "Manzoor Hussain"
print(Counter(name).most_common(1)) # returns the most common alphabet
