# Write a Python program using nested loops to print the following pattern of odd numbers:
# 1
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9

for i in range(1,6):
    for j in range(1,i+1):
            print(2*j-1,end=" ")
    print()

