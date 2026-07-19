file = open(r"C:\Users\hp\PycharmProjects\PythonDEMO\Filehandling\age","r")

for i in file:
 data=i.rstrip('\n').split(",")
 age = int(data[3])
 # if age >= 22:
 #      print(data)
 loc = data[5].strip()
 # if loc == "Delhi":
 #     print(data[1:5:2])
 if age>=22 and loc =="Chennai":
     print(data[1::2])
