# 9. Salary Report Generator
#
# A company wants a salary report for its employees.
#
# Rules:
#
# First, enter the number of employees.
#
# Then enter the salary of each employee.
#
# If salary is greater than 50,000, count them as high salary.
#
# If salary is 50,000 or less, count them as low salary.
#
# Display:
#
# Number of employees earning above 50,000
#
# Number of employees earning 50,000 or below


num_employee = int(input("enter the number of employee: "))
count_high = 0
count_low = 0
for i in range(1,num_employee+1):
    sal = int(input(f"enter the salary of employee{i}:"))
    if sal >50000:
        count_high+=1
    else:
        count_low+=1
print("Number of employees earning above 50,000: ",count_high)
print("Number of employees earning 50,000 or below : ",count_low)
