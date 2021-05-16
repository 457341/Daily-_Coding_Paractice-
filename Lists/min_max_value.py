def min_max_value(lst):
    min_value = min(i for i in lst if isinstance(i, int))
    # min_value = min(list(i for i in lst if isinstance(i, int))) # both works same
    max_value = max(i for i in lst if isinstance(i, int))

    print(f"Min value is: '{min_value}' and max value is: '{max_value}'   ")
lst = ['manzoor','xyz',2,3,4,5,'xy']
min_max_value(lst)