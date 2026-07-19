# Question 2: Palindrome Checker
# Problem: Write a program to check if a word entered by the user is a palindrome (reads the same forward and backward). Ignore case sensitivity.
# Input: Radar
# Output: It is a palindrome!
word = input("enter the word: ")
word = word.lower()
print(word[::-1])
if word == word[::-1]:
    print("palindrome")
else:
    print("Not palindrome")