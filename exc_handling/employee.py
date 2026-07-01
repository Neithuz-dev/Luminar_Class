# try:
#     employee = {"name":"abin"}
#     print(employee["age"])
# except KeyError:
#     print("Key not found")
try:
    ls = [8,9,3,4]
    print(ls[8])
except IndexError:
    print("Index not found")