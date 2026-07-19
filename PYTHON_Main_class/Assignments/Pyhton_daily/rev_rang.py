# Write a Python program to print the reverse of each number in the range from 34 to 56.
# Example: Input: 34   -> Output: 43  (reverse of 34)
# Input: 56   -> Output: 65  (reverse of 56)
def rev_rang():
    for num in range(34,57):
        rev  =str (num)[::-1]
        print(f"{rev}(reverse of {num})")

rev_rang()
