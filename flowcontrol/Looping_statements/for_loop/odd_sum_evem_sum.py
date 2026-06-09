lower = int(input("enter the lower limit"))
upper = int(input("enter the upper limit"))
sum_even = 0
sum_odd = 0
for i in range (lower,upper+1):
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
print(f"the sum of even is {sum_even}")
print(f"the sum of odd is {sum_odd}")
