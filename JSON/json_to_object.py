import json
student_info = '{"name":"Manzoor","Surname":"Hussain","Country":"Pakistan"}'
student_obj = json.loads(student_info)
print(student_obj["name"])
print(student_obj["Surname"])
print(student_obj["Country"])

print(student_obj)
print(student_info)