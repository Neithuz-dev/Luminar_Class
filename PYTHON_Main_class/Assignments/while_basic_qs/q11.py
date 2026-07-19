# 11. Employee Salary Entry
# Question
# An HR staff enters employee salaries.
# Stop entering when salary -1 is entered.
# Find total salary expense.
employee_salary = int(input("enter the salary: "))
total_salary = 0
while employee_salary > 0:
    employee_salary = int(input("enter the salary: "))
    total_salary+=employee_salary
print(f"total salary expense:{total_salary}")