text = "Welcome"
Vowels = "aeiou"
count = 0
for i in text.lower():
    if i in Vowels:
        count+=1
print(count)