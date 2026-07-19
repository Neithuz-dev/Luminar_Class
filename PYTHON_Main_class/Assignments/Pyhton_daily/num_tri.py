# Write a Python program using nested loops to print the following pattern, where each row's leading numbers repeat the row number and the remaining numbers count up to 5:
# 1	2 3 4 5
# 2	2 3 4 5
# 3	3 3 4 5
# 4	4 4 4 5
# 5	5 5 5 5

for i in range(1,6):
    for j in range(1,6):
        if j < i:
            print(i, end = " ")
        else:
            print(j , end = " ")
    print()