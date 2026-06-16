def even_odd_sum(lower,upper):
    even_sum = 0
    odd_sum = 0
    for i in range(lower,upper+1):
        if i%2==0:
            even_sum+=i
        else:
            odd_sum+=i
    return even_sum,odd_sum
rs1,rs2 = even_odd_sum(2,8)
print("even sum",rs1)
print("odd sum",rs2)