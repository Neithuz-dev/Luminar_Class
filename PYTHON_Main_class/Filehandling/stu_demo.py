file1 = open(r"C:\Users\hp\PycharmProjects\PythonDEMO\Filehandling\stu_name","r")
file2 =open("student","w")
for i in file1:
    file2.write(i)