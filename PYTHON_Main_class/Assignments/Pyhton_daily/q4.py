# Write a Python program using nested loops to print the following pattern, where each row counts down from the row number to 1:
# 1
# 2	1
# 3	2 1
# 4	3 2 1
# 5	4 3 2 1
for i in range(1,6):
    for j in range(1,i+1):
         print((i+1)-j,end = " ")
    print()