# n = int(input("enter the number: "))
# factorial = 1
# for i in range (1 , n+1):
#     factorial = factorial * i
# print(factorial)

n = int (input("enter the number : "))
fact = 1
for i in range(1,n+1):
    fact += fact*i
print(fact)