# Question 5: Apply a 10% Discount on Expensive Products
# Question
# Display only products costing more than ₹1000 and apply a 10% discount.
prices = [500, 1200, 800, 2000, 1500]
# Output: [1080.0, 1800.0, 1350.0]
ls = list(map(lambda x:x-(x*10/100), filter(lambda x:x>1000,prices)))
print(ls)
