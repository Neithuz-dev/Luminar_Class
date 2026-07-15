for i in range(34,57):
    temp = i
    rev = 0
    while temp >0:
        digit = temp%10
        rev = rev*10+digit
        temp = temp//10
    print(i ,"->",rev)
