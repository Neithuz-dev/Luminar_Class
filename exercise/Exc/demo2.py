string = "Data Analytics is a growing field with Many Oppertunities"
string = string.lower()
count_vow=0
count_con = 0
for i in string:
    if i.isalpha():
        if i in "aeiou":
            count_vow+=1
        else:
            count_con+=1
print(count_vow,count_con)
