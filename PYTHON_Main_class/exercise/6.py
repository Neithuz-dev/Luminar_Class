#check whether the sum of 2 number is between 20 and 50
n1 = int(input("enter the 1st number: "))
n2 = int(input("enter the second number: "))
sum = n1+n2
print(sum)
print(f"The {sum} is",20<=sum<=50)