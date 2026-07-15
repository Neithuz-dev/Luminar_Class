for i in range(23,101):
    count = 0
    for j in range(1,i):
        if i%j ==0:
            count+=j
        else:
            pass
    if count ==i:
        print(i)