# You are auditing an election for class president. The votes are stored as strings in a tuple. Write a program that counts exactly how many votes "John" and "Sara" received individually, and print the results.
#
# input:
# votes = ("John", "Sara", "John", "Maya", "Sara", "John", "John", "Alex")
#
# Output:
# John received: 4 votes
# Sara received: 2 votes

votes = ("John", "Sara", "John", "Maya", "Sara", "John", "John", "Alex")
count_john = 0
count_sar = 0
for i in votes :
    if i == "John":
        count_john += 1
    elif i =="Sara":
        count_sar+= 1
print("John received:",count_john)
print("Sara received",count_sar)