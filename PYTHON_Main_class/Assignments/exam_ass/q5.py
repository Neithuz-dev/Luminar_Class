strt = int(input("enter the start number:"))
end = int(input("enter the last number:"))
count = 0
for i in range(strt,end+1):
    count = 0
    for digit in str(i):
        if digit =="2":
            count+=1
    if count ==2:
        print(i)