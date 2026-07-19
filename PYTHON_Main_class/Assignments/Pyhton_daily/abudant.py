# Write a Python program to input a number and check whether it is an Abundant Number or not. A number is called an Abundant number if the sum of its proper factors (i.e., divisors excluding the number itself) is greater than the number itself.
# Example: Input: 12
# Factors of 12 (excluding 12) = 1, 2, 3, 4, 6
# Sum of factors = 1 + 2 + 3 + 4 + 6 = 16
# Since 16 > 12, output: "12 is an Abundant number"
n = int(input("enter the number:"))
total = 0

for i in range(1,n):
    if n%i ==0:
        total +=i

if total >n:
    print(f"{n} is an Abundant number")
else:
    print("Not Abundant number")