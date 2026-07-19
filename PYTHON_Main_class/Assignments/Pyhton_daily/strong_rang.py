# Write a Python program to print all Strong Numbers between 45 and 97.
# A number is called a Strong number if the sum of the factorials of its digits equals the number itself.
# Example: e.g. 145 is a strong number because 1! + 4! + 5! = 1 + 24 + 120 = 145

for i in range(45 , 98):
    num =i
    total = 0
    while num >0:
        digit = num%10
        fact = 1
        for j in range(1,digit+1):
            fact = fact*j
        total +=fact
        num =num//10
    if total == i :
        print(i)
else:
    print("No strong numbers")
