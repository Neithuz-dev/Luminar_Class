file = open(r"C:\Users\hp\PycharmProjects\PythonDEMO\Filehandling\roles","r")
d={}
for i in file:
    data = i.rstrip('\n').split()
    for job in data:
        if job not in d:
            d[job]=1
        else:
            d[job]+=1
print(d)