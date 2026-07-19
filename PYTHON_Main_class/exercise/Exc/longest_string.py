from shlex import split

words= "APJ abdul Kalam Tehchnical university"
s= words.split()
longest =""

for i in s:
    if len(i)>len(longest):
        longest = i

print(longest)
