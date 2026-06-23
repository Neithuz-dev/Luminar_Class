company = "Luminar Technolab"
count = 0
ls_conso = []
for char in company:
    if char.isalpha():
        if char not in "aeiou":
            count +=1
            ls_conso.append(char)
print(count)
print(ls_conso)