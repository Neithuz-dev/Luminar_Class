for i in range(1,6):
    for j in range(1,6):
        #1 +0 =1 1+1=2 , 2+0=2 2+1=3
        if i > j:
            print(i , end = " ")
        else:
            print(j ,end = " ")
    print()