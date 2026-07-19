# n = int(input("enetr the number :"))
# temp =n
# count = 0
# while temp > 0:
#     count += 1 #1 2 3 4
#     temp = temp // 10 #163 16 1 0
#
# temp = n #1634
# total = 0
#
# while temp > 0:
#     digit = temp % 10 #4  3 6
#     total = total + digit ** count #0+4**4= +3**4==  6**4
#     temp = temp // 10#163 16
#
# if total == n: #1634==1634
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")
# n = int(input("enetr the number :"))
# temp =n
# count = len(str(n))
# total = 0
#
# while temp > 0:
#     digit = temp % 10 #4  3 6
#     total = total + digit ** count #0+4**4= +3**4==  6**4
#     temp = temp // 10#163 16
#
# if total == n: #1634==1634
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")

n = int(input("enter the number : "))
count = len(str(n))
total = 0
temp = n
while n>0:
    digit = n%10
    total += digit**count
    n = n//10
if total == temp :
    print("armstrong")
else:
    print("not Armstrong")
