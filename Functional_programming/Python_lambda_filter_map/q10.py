# Question 10: Process Bank Transactions
# Question
# Display only deposits (positive values) and add a ₹100 cashback to each deposit.
transactions = [1000, -500, 2000, -300, 1500]
# Output: [1100, 2100, 1600]
ls = list(map(lambda x:x+100,filter(lambda x:x>0,transactions)))
print(ls)