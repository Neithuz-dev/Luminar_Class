# Question: Write a password validator program. A valid password must meet the following criteria:
# Must be at least 8 characters long.
# Must contain at least one uppercase letter.
# Must contain at least one lowercase letter.
# Must contain at least one digit.
# The program should print whether the password is valid or valid reasons why it failed.
password = input("enter the password: ")
length = len(password)
upper = 0
lower =0
digit =0
for ch in password:
    if ch.isupper():
        upper+=1
    if ch.islower():
        lower+=1
    if ch.isdigit():
        digit+=1
if length>=8 and upper>0 and lower>0 and digit>0:
    print("Valid Password")
else:
     print("Invalid password")
