ls = [(i**2) if i%2==0 else (i,i**3) for i in range(1,26)]
print(ls)


name = "abinaya"
vow = "aeiou"
ls1 = [i for i in name.lower() if i in vow]
print(ls1)