# # 6. Phone Unlock System
# # Question
# # A mobile phone allows only 3 password attempts.
# # If the correct password is "1234", display "Phone Unlocked".
# # Otherwise display "Phone Blocked".
attempts = 1
while attempts <= 3 :
    password = input("enter the password :")
    if password =="1234":
        print("Phone Unlocked")
        break
    else:
        print("Incorrect Password")
    attempts += 1

if attempts > 3:
    print("phone blocked")
