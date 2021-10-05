import pandas as pd 
from tabulate import tabulate
import numpy as np
amzn_data = pd.read_csv('HistoricalData_AAPL.csv')
# print(amzn_data.head(1))
print(tabulate(amzn_data.head(), headers='keys', tablefmt='psql'))
print(tabulate(amzn_data.describe(),headers='keys', tablefmt='psql'))
# making dataframe 
df = pd.DataFrame({"alphabets":['a','b','c','d','e'],"vowels":['a','e', 'i', 'o', 'u']})
# print(df.head())
print(tabulate(df.head(),headers='keys', tablefmt='psql'))
marks = pd.DataFrame({'Math':[100,50,60,80],'English':[20,90,30,50]})
print(marks.head())
#? Pandas Series
names = pd.Series({'names':['name1','name2','name3']}) #! Wrong : In series we don't have to put the name of column
print(names.head())
names2 = pd.Series(['name1','name2','name3']) #? True
print(names2.head())
names3 = pd.Series(['name1','name2','name3'],name='Studets') # Putting column name
print(names3.head())
# Creating DataFrame 
df = pd.DataFrame({'names':['name1','name2','name3'],'schools':['school1','school2','school3']})
print(df.head())
s = pd.Series(['s1','s2','s3'])
print(s)
df1 = pd.DataFrame({'column1':['r1','r2','r3','r4'],'column2':['r1','r2','r3','r4']})
print(df1)
