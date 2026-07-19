# Write a Python program to check whether a given number is a Circular Prime. A number is called a circular prime if every rotation of its digits also results in a prime number.
# Example: Input: 197
# Rotations: 197, 971, 719
# All three rotations are prime numbers
# Output: "197 is a circular prime" *
num = input("Enter a number: ")
circular = True
for i in range(len(num)):
    rotation = num[i:] + num[:i]
    n = int(rotation)
    prime = True
    if n <= 1:
        prime = False
    else:
        for j in range(2, n):
            if n % j == 0:
                prime = False
                break

    if not prime:
        circular = False
        break
if circular:
    print("Circular Prime")
else:
    print("Not a Circular Prime")