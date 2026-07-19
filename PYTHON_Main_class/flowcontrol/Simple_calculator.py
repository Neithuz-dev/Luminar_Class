# Write a Python program that acts as a simple calculator.
#
# The program should:
# Ask the user to enter two numbers.
# Ask the user to enter an operator (+, -, *, or /).
# Perform the corresponding operation based on the operator entered.
# Display the result of the operation.
# If the user tries to divide by zero, display an error message saying “Division by zero not allowed.”
# If the user enters an invalid operator, display “Invalid operator.”
num1 = int(input("enter two numbers : "))
num2 = int(input())
operat = input("enter the operator: ")
if operat == "+":
    print(num1+num2)
elif operat == "-":
    print(num1-num2)
elif operat == "*":
    print(num1*num2)
elif operat == "/":
    if num2 == 0:
        print("Division by zero not allowed")
    else:
        print(num1/num2)
else:
    print("Invalid operator.")
