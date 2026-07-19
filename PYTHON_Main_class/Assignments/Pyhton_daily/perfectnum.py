# Write a Python program to check whether a given number is a Perfect Number. A number is called perfect if the sum of its proper divisors (excluding itself) equals the number itself.
# Example: Input: 6
# Divisors of 6 (excluding 6) = 1, 2, 3
# Sum = 1 + 2 + 3 = 6
# Since sum equals the number, output: "6 is a Perfect Number"
def perfect(num):
    total = 0
    for i in range(1,num):
        if num %i ==0:
            total +=i

    if total == num:
        return "Perfect Number"
    else:
        return "not perfect Number"
num  = int(input())
print(perfect(num))
