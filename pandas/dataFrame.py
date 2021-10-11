#Pandas Dataframe
import pandas as pd
import numpy as np
df = pd.DataFrame({"X":[1,2,3,4,5],"Y":[11,12,13,14,15],"Z":[10,20,30,40,50]})
print(df.head())
df2 = pd.DataFrame({"Name":['Manzoor',"Mazhar","Ali","Hamid","Nadir"],
                    "Score":[12.5,9,16.5,np.nan,100],
                    "Attempts":[1,2,3,2,1],
                    "Quality":['Yes','No','Yes',"No","Yes"]},index=['a','b','c','d','e'])
print(df2.head())
#Summary of DataFrame
print(df2.info())
# Selecting some specific columns
print(df2["Name"].head()) # Works 
# print(df[["Name"]].head()) # Not work
# print(df2["Name","Score"].head()) #  Not Work
# print(df2[["Name","Score"]].head())

# Write a Pandas program to count the number of rows and columns of a DataFrame. Go to the editor
# Sample Python dictionary data and list labels:
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 1[12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19]9],
# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# Expected Output:
# Number of Rows: 10
# Number of Columns: 4
name = ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas']
score = [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19]
attempts = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
qualify = ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df3 = pd.DataFrame({"name":name,"score":score,"attempts":attempts,"qualify":qualify},index=labels)
print(df3.head())
print("Total Columns in DataFrame: ",len(df3.columns)) # Counting total number of columns in dataframe
print("Total rows in DataFrame: ",len(df3["name"]))


# Write a Pandas program to select the rows where the score is missing, i.e. is NaN
null_values_column = df3[df3["score"].isnull()]
print(null_values_column)
#select the rows the score is between 15 and 20 (inclusive).
print(df3[df3['score'].between(15, 20)])

# Deleting attempts columns
df3.drop(['attempts'],axis=1,inplace=True)
print(df3.head())
# Adding new column
print(len(df3['name']))
df3['color'] = ['Red', 'Green', 'White', 'Black','Blue','Magenta','Yellow','YellowGreen','Orange','GreenYellow']
print(df3.columns)
# Iterating over rows
for index, row in df3.iterrows():
    print(row['name'],row['score'])

# Rename Column Names
df3.rename(columns={"name":"Ad","score":"Skor","color":"Renk","qualify":"Qualify"},inplace=True)
print(df3.columns)

# Selectiong rows on the basis of same column values
d = pd.DataFrame({'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]})
print(d.loc[d['col1']==4])
# Altering columns
d = d[['col3','col2','col1']] 
print(d.head())
# Saving File as csv (Comma Separated File)
d.to_csv('demo.csv')
new_df = pd.read_csv('demo.csv',index_col=0)
print(new_df.head())
# combining two series
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series(['a', 'b', 'c', 'd', 'e'])
concated = pd.concat([s1, s2],axis=1)
print(concated.head())
