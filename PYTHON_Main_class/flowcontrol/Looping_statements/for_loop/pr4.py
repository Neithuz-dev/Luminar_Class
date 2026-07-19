# Count even and odd digits in a number
n = int(input("enter the number: "))
count = len(str(n))
count_even =0
count_odd = 0
for i in range(count):
    if n>0:
        digit = n%10
        if digit%2==0:
            count_even +=1
        else:
            count_odd+=1
        n=n//10
print("The number of even is",count_even)
print("The number of odd is",count_odd)
