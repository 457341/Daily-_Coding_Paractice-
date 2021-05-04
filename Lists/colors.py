#  Write a Python program to convert list to list of dictionaries. 
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

def convert_color(colors,color_codes):
    color_info = []
    # color_info.append(colors)
    new_color = {}
    for i in range(4):
        # print(i)
        color = colors[i]
        code = color_codes[i]
        new_color["color_name"] = color
        new_color["color_code"] = code
        color_info.append(new_color)
        new_color = {}
    # print(new_color)


    print(color_info)
colors = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
convert_color(colors,color_codes)
