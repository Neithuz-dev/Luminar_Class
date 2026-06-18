s= "I love to code"
result =""

for i in s:
    if i not in result:
        result += i
print(result)