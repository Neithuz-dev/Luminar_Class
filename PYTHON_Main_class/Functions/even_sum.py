def even_sum(n):
    even_total = 0
    for i in range(1,n+1):
        if i%2==0:
            even_total+=i
    return even_total

res = even_sum(5)
print(res)#2+4+