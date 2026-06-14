# 1.Take a number n and print the square of each number from 1 to n.
n = int(input("enter the number: "))
for i in range(1,n+1):
    print(f"Square of {i}",i*i*i)