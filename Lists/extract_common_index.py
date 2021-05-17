#  Write a Python program to extract common index elements from more than one given list. Go to the editor
# Original lists:
# [1, 1, 3, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 5, 7]
# [0, 1, 2, 3, 4, 5, 7]
# Common index elements of the said lists:
# [1, 7]

def extract_common_index(l1, l2,l3):
    common_index = []
    for a,b,c in zip(l1,l2,l3):
        if a == b == c:
            common_index.append(a)
    print(common_index)
l1 =  [1, 1, 3, 4, 5, 6, 7]
l2 = [0, 1, 2, 3, 4, 5, 7]
l3 = [0, 1, 2, 3, 4, 5, 7]
extract_common_index(l1, l2, l3)
