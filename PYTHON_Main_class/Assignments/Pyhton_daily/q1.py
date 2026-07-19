# Q16. Right-Aligned Star Triangle
# Write a Python program using nested loops to print the following right-aligned star triangle pattern:
# *
# *	*
# *	* *
# *	* * *
# *	* * * *

for i in range(6):
    for j in range(i):
        print("*",end = " ")
    print()