# Write a Python program that first checks if the entered username is admin. If the username is correct, then inside that condition check whether the password is secret123. If both match, print "Access granted". Otherwise, print the appropriate error message.
username = input("enter the user name: ")
password = input("enter the password: ")

if username == "admin":
    if password == "secret123":
        print("Access granted")
else:
    print("Error")