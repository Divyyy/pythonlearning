# key value pairs and allow fast hookups
marks = {"HArry": 34, "Divyam": 30, "jack":45,"lily": 89}
print(marks,type(marks))
print(marks["Divyam"])
marks["Divyam"]=70
print(marks)
print(marks.keys())
print(marks.values())
marks.pop("lily")
print(marks)

table_of_5 ={i: 5*i for i in range(1,11)}
print(table_of_5)