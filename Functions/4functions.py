def add(num1,num2):
    add = num1+num2
    return "Addition: ",add
def sub(num1,num2):
    sub = num1-num2
    return "Subtraction: ",sub
def div(num1,num2):
    divide = num1/num2
    return f"Divide: {divide}"
def mult(num1,num2):
    mul =num1*num2
    return mul

num1 = int(input("enter the number 1: "))
num2 = int(input("Enter the number 2: "))
oper = int(input("Press 1. for addition \n 2.for subtraction \n 3.Division \n 4.Multiplication \n"))
if oper ==1:
    res1 = add(num1,num2)
    print(res1)
elif oper ==2:
    res2 =sub(num1,num2)
    print(res2)
elif oper == 3:
    res= div(num1,num2)
    print(res)
elif oper == 4:
    res4 = mult(num1,num2)
    print(res4)
else:
    print("Invalid number")