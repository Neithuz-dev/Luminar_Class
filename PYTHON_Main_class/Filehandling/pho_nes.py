file1 = open(r"C:\Users\hp\PycharmProjects\PythonDEMO\Filehandling\phones","r")
file2 =open("Phones_names","w")
for i in file1:
    if i != "samsung\n":
        file2.write(i)
