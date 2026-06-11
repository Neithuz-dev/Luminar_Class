# Question 1: Username Generator
# Problem: Ask the user to input their first name and last name. Create a username by taking the first 3 letters of the first name and the last 3 letters of the last name.
# Input: First: Alexander, Last: Smith
# Output: Aleith
First = input("name")
last = input("name")
print(First[:3:]+last[-3:])