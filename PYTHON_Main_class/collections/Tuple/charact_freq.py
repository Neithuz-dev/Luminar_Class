# A text-processing application needs to analyze the frequency of characters in a sentence.
# Write a Python program that:
# 1.	Accepts a string from the user.
# 2.	Ignores spaces and non-alphabetic characters.
# 3.	Finds the frequency of each character.
# 4.	Displays each character only once along with its count.
# 5.	Maintain the order of first appearance.
# Input
# str = input("enter the string:")
# new_list = []
#
# for  char in str:
#     if char.isalpha() and char not in new_list:
#         count = str.count(char)
#         new_list.append((char,count))
#
# print(new_list)
# Output
# [('p', 2), ('y', 1), ('t', 1), ('h', 1), ('o', 2), ('n', 2), ('r', 2), ('g', 2), ('a', 1), ('m', 2), ('i', 1)]

str = "python programming"
result = []

for  char in str:
    if char.isalpha():
         count = str.count(char)
         if (char,count) not in result:
            result.append((char,count))

print(result)