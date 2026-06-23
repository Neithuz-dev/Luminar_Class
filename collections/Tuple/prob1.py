# Element Checker
# colors = ("red", "blue", "green", "yellow", "purple")
#
# Input/Output Example 1:
# Enter a color to search: Blue
# Found!
colour = input("enter the colour:  ")
colors = ("red", "blue", "green", "yellow", "purple")

for word in colors:
    if word == colour.lower():
        print("Found!")