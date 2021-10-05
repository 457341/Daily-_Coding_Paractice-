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