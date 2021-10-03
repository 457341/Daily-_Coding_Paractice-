#? Question 1
#  1. Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.
# df = pd.DataFrame({'names': ['name1','name2','name3']})
# print(df.head())
import pandas as pd
import numpy as np
s = pd.Series([1,2,3])
print(s)
#? Question2:
# 2. Write a Pandas program to convert a Panda module Series to Python list and it's type.
#! Answer
s1 = pd.Series([1,2,3,4,5])
lst = list(s1)
print(lst)
print(type(lst))
#? Question3:
# Write a Pandas program to add, subtract, multiple and divide two Pandas Series
#! Answer
s3 = pd.Series([2,4,6,8,10])
print(s3+1, s3*2,s3-0,s3/2)
# Write a Pandas program to convert a dictionary to a Pandas series.
dic = {'a':1, 'b':2, 'c':3}
dic_to_series = pd.Series(dic)
print(dic_to_series)
# Write a Pandas program to convert a NumPy array to a Pandas series
arr = np.array(['a','e', 'i', 'o', 'u'])
arr_to_series = pd.Series(arr)
print(arr_to_series)
###
