# Question 1: Find Expensive Products
# Question
# Display products whose price is greater than ₹1000.
prices = [800, 1500, 2000, 500, 1200]
# Output: [1500, 2000, 1200]
ls  = list(filter (lambda x:x>1000,prices))
print(ls)