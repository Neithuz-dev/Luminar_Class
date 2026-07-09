# Question 11: Process Student Names
# Question
# Display only names having 4 or more characters and convert them to lowercase.
names = ["ANU", "RAHUL", "JO", "DIVYA", "RAM"]
# Output: ['rahul', 'divya']
ls = list(map(lambda x:x.lower(),filter(lambda x:len(x)>=4,names)))
print(ls)
