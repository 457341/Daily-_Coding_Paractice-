# Write a Python program that iterate over elements repeating each as many times as its count.

from collections import Counter
c = Counter(p=4, q=2, r=0, s=-2)
d = Counter(d =4)
print(list(c.elements()))
print(tuple(d.elements()))
# Write a Python program to find the most common elements and their counts of a specified text.
name = "Manzoor Hussain"
print(Counter(name).most_common(1)) # returns the most common alphabet
# Write a Python program to create a new deque with three items and iterate over the deque's elements.
from collections import deque
d = deque("aeiou")
for i in d:
    print(i)
import re
text = """The Python Software Foundation (PSF) is a 501(c)(3) non-profit 
corporation that holds the intellectual property rights behind
the Python programming language. We manage the open source licensing 
for Python version 2.1 and later and own and protect the trademarks 
associated with Python. We also run the North American PyCon conference 
annually, support other Python conferences around the world, and 
fund Python related development with our grants program and by funding 
special projects."""
words = re.findall('\w+',text)
print(Counter(words).most_common(10))
