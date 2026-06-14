# 6.Employee Salary Bonus Calculation
#
#  Rules:
#
#  Salary > 50,000 → 10% bonus
#
#  Salary ≤ 50,000 → 5% bonus
salary = int(input("Enter employee salary: "))
if salary > 50000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05
total_salary = salary + bonus
print("Salary:", salary)
print("Bonus:", bonus)
print("Total Salary:", total_salary)