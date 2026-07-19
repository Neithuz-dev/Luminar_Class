n = int(input("enetr the number: "))
i = n
rev = 0
while i>0:
    digit = i%10
    rev = rev*10+digit
    i=i//10
if n == rev :
    print("palindrome")
else:
    print("Not palindrome")
