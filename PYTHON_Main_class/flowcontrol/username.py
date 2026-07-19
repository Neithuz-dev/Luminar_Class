username = input("enter the user name: ")
password = input("enter the password: ")

if username == "admin":
    if password == "secret123":
        print("Access granted")
else:
    print("Error")