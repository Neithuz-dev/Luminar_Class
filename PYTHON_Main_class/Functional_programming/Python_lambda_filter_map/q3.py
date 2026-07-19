# Question 3: Double the Even Numbers
# Question
# Find all even numbers from the list and double their value.
numbers = [5, 8, 11, 14, 20, 25]
# Output: [16, 28, 40]

ls = list(map(lambda x:x*2,filter(lambda x:x%2==0 , numbers)))
print(ls)