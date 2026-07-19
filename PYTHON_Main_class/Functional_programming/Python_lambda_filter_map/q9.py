# Question 9: Increase the Price of Low-Cost Products
# Question
# An online store wants to increase the price of products costing less than ₹500 by ₹50.
prices = [250, 600, 450, 800, 300]
# Output: [300, 500, 350]
ls = list(map(lambda x:x+50,filter(lambda x:x<500,prices)))
print(ls)