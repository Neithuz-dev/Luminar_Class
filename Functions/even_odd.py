def even_odd_sum(lower,upper):
    even_sum = 0
    odd_sum = 0
    for i in range(lower,upper+1):
        if i%2==0:
            even_sum+=i
        else:
            odd_sum+=i
    print("even sum ",even_sum)
    print("Odd sum", odd_sum)


even_odd_sum(2,8)