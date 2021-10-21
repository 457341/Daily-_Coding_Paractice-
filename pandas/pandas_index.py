import pandas as pd
students = pd.DataFrame({
    "Name":['Manzoor','Ali','Ahmed'],
    "University":['Omu','Odtu','Eru'],
    "Class":[1,2,4],
    "City":['Istanbul','Ankara','Samsun'],
    "roll_no":  ['S01','S02','S03']
})
ogrenci_no = ['a', 'b', 'c']
print(students)
students = students.set_index('roll_no') # Changing the index Number
print()
print(students)
# students  = students.set_index('ogrenci_no') # Changing the index Number 
# if we want to change the index number, it must be any column
print()
print(students)

# todo: Indexing using two columns
print()
students = students.set_index(['City','Class']) # Making two index
print(students)
# change the index name
students.index.name = 'INDEX'
print(students)
#
print('t4' in students.index.levels[0])
