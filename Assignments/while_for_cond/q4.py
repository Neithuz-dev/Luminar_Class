# 4.Count even and odd digits in a number
count_even = 0
count_odd = 0
n = int(input("enter the number: "))
length = len(str(n))
for i in range(length):
    digit = n%10
    if digit%2==0:
        count_even+=1
    else:
        count_odd+=1
    n=n//10
print(f"Count even:{count_even} and Count odd: {count_odd} ")