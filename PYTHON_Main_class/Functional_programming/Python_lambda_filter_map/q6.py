# Question 6: Convert Long Words to Uppercase
# Question
# Display only words that have more than 5 characters, then convert them to uppercase.
words = ["apple", "elephant", "cat", "notebook", "pen"]
# Output: ['ELEPHANT', 'NOTEBOOK']
ls = list(map(lambda x:x.upper(),filter(lambda x:len(x)>5,words)))
print(ls)
