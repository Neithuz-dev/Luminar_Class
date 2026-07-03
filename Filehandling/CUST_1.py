file = open(r"C:\Users\hp\PycharmProjects\PythonDEMO\customer1.txt","r")

for i in file:
    data = i.rstrip().split(",")
    # print(data)
    #1
    # prof = data[4]
    # if prof =="Dancer":
    #     print(data)
    #2
    # age =int(data[3])
    # if  age > 50:
    #     print(data[1:4:])
    #3
    # if age >25 and age <40:
    #     print(data[1:4:])
    #4
    loc = data[5]
    if loc == "india":
        print(data[1:5:])