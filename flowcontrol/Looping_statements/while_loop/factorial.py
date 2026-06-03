#fact 3= 3*2*1
#4 = 4*3*2*1
n= int(input("enter the number :"))
i=1
fact=1
while i<=n:
    fact=fact*i #1*1=1, 1*2=2 ,2*3=6
    i+=1
print(fact)