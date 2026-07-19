# Write a Python program to print all Perfect Numbers between 23 and 100.
# Example: Range: 23 to 100
# Output: 28  (28 = 1 + 2 + 4 + 7 + 14)
def perf_rang():
    for i in range(23 , 101):
        total_fac = 0
        for j in range(1,i):
            if i %j == 0:
                total_fac+=j

        if total_fac == i:
            print(i)

perf_rang()