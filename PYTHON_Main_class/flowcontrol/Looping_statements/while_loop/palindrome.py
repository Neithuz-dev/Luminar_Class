n = int(input("enter the number"))
# i = n
# rev = 0
# while i>0:
#     digit = i%10
#     rev = rev*10+digit
#     i=i//10
# if rev == n:
#     print("palindrome")
# else:
#     print("Not palindrome")
rev = 0
temp = n
while n>0:
    digit = n%10
    rev = rev*10+digit
    n = n//10
if rev == temp:
    print("palindrom")