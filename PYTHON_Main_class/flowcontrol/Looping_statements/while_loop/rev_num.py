n = int(input('enter the number:'))#123
rev = 0
while n>0:
    digit=n%10 #3 2
    rev = rev*10+digit#0+3 =3 ,3*10+2=32
    n=n//10
print(rev)
