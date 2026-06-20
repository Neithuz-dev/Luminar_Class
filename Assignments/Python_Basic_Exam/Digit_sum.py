# The Digit Sum Extractor
# Problem Description: Write a program that asks the user to enter a mixture of text and numbers.
# The program must look at every character, extract only the numerical digits, calculate their total
# sum, and print the result.
# Example:
#  Input: abc5xyz3q2
#  Output: Sum of digits: 10 (Calculated as 5 + 3 + 2)

string = "abc5xyz3q2"
sum = 0
for char in string:
    if char.isdigit():
        sum+= int(char)
print(sum)