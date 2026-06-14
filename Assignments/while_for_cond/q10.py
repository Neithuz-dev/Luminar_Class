# 10. Check Armstrong Number
#
# An Armstrong number is a number where:
#
# The sum of the cube of each digit is equal to the original number.
#
# Example:
#
# 153 → 1³ + 5³ + 3³ = 153 ✔
#
# Your task:
#
# Enter a number
#
# Check whether it is an Armstrong number or not
num = int(input("enter the number: "))
temp1 = num
count = len(str(num))
sum_arm =0
for i in range(count):
    digit = temp1%10
    sum_arm +=digit**count
    temp1 = temp1//10
if num == sum_arm:
    print("Armstrong")
else:
    print("Not Armstrong")
