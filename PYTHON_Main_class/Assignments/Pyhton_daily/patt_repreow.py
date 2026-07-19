# Write a Python program using nested loops to print the following pattern, where each row number is repeated as many times as the row number itself:
# 1
# 2	2
# 3	3 3
# 4	4 4 4
# 5	5 5 5 5
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end = " ")
    print()