# 0
# 1 1
# 2 3 5
# 8 13 21 34
# n = int(input("enter the number: "))
# num1=0
# num2 = 1
# for i in range(1,n+1):
#     for j in range(i):
#         print(num1, end=" ")
#         sum1 = num1+num2
#         num1=num2
#         num2=sum1
#     print()

n =  int(input("enter the number: "))
num1= 0
num2 = 1
for i in range(1,n+1):
    print(num1,end=" ")
    sum =num1+num2
    num1 = num2
    num2 = sum

