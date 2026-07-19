# Question 12: Process Product IDs
# Question
# Display only product IDs greater than 1000 and convert them into strings by adding the prefix "PID-".
ids = [850, 1200, 950, 1800, 2200]
# Output: ['PID-1200', 'PID-1800', 'PID-2200']
ls = list(map(lambda x:f"PID-{x}",filter(lambda x:x>1000,ids)))
print(ls)