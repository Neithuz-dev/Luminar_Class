# Write a Python program to print all numbers within a given range that contain the digit 2 at least twice.
# Example: Range: 1 to 210
# Output: 22, 122, 202
def cont():
    for i in range(1,211):
        count = 0
        for digit in str(i):
            if digit == "2":
                count+=1
        if  count >=2:
            print(i)
cont()