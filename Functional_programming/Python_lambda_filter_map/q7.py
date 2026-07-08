# Question 7: Find Adult Ages and Categorize Them
# Question
# Display only people aged 18 years or above. Then classify them:
# 18–59 → Adult
# 60 and above → Senior Citizen
ages = [12, 18, 25, 61, 15, 70]
# Output: ['Adult', 'Adult', 'Senior Citizen', 'Senior Citizen']
ls = list(map(lambda x:"Adult" if x<=59 else "senior citizen"  ,filter(lambda x:x>=18,ages)))
print(ls)