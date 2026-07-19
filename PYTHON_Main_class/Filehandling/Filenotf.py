try:
    file = open(r'C:\Users\hp\PycharmProjects\PythonDEMO\Filehandling\subjcts_023')
    for i in file:
        print(i)
except FileNotFoundError:
    print("path not Found")