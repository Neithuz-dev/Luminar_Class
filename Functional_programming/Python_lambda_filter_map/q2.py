# Question 2: Increase the Salary of Low-Paid Employees
# Question
# A company wants to give a ₹5,000 bonus only to employees whose salary is less than ₹30,000.
salary = [25000, 42000, 18000, 55000, 27000]
# Output: [30000, 23000, 32000]

ls = list(map(lambda x:x+5000,filter (lambda x:x<30000,salary)))
print(ls)

