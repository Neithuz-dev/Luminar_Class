file = open(r"C:\Users\hp\PycharmProjects\PythonDEMO\reg\order_data.csv","r")
# print(file.read())
# next(file)
import re
count_p=0
for i in file:
    data = i.rstrip()
    # data = re.findall(r"ORD\d+",i)
    # print(data)
    # if re.search("Laptop",i):
    #     print(i.strip())
    # if re.search("Completed",data):
    #     print(data)
#     if re.search("Pending",data):
#         count_p+=1
# print("Total Pending Orders",count_p)
    amount = re.search(r"\d+",data)
    if int(amount[2]) >50000:
        print(data)


