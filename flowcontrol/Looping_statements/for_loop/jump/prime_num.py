lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
for num in range(lower, upper + 1): #12 
    if num > 1:#12>1
        for i in range(2, num):#i=2 ,3
            if num % i == 0:#12%2==0
                break
        else:
            print(num, "is prime")