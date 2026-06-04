# Find the largest digit in a number.
#
# Example: 5837 → 8
n = int(input("enter the number : "))
large = 0
while n>0:
    digit = n%10
    if digit>large:
        large = digit
    n = n//10
print(large)