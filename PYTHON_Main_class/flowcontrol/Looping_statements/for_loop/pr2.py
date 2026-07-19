#Count how many numbers are divisible by 3 between lower and upper
lower = int(input("enter the lower limit: "))
upper = int(input("enter the upper limit: "))
count = 0
for i  in range(lower,upper+1):
    if i%3==0:
        count+=1
print(f"Count of number div by 3:{count}")