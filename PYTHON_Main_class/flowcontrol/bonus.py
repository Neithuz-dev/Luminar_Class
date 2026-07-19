#calculate bonus check if the employee have more than 5 years of exp
salary=int(input("enter the salary"))
exp =int(input('enter the no of years of exp'))
if exp>5:
    bonus= salary*(5/100)
    print("Bonus is ",bonus)
else:
    print("No bonus")
