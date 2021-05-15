# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["year"] = 2020
def unique_sublists(input_list):
    result ={}
    for l in input_list: 
        result.setdefault(tuple(l), list()).append(1) 
        # print(result)
    for a, b in result.items(): 
        # print(a,b)
        result[a] = sum(b)
    # return result
    print(result)

list1 = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] 
unique_sublists(list1)