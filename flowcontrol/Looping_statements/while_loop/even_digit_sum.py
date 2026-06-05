#even digit sum
n = int(input("Number:"))
even_count = 0
while n> 0:
    digit = n%10
    if digit%2 == 0 :
        even_count+=1
    n = n//10
print(even_count)