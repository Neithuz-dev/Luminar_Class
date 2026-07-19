file = open(r"C:\Users\hp\PycharmProjects\PythonDEMO\Filehandling\temper.txt","r")
# print(file.read())
d = {}

for i in file:
    data = i.rstrip().split(",")
    place = data[0]
    temp = data[1]
    # print(data)
    if place not in d:
        d[place] =temp
    else:
      old =d[place]
      if temp >old:
        d[place]= temp
print(d)

