# Question 9
# The Password Reset Lockout
# Problem: A user is trying to reset their password. They must enter their old password correctly to
# proceed. Set a variable old_password = &quot;password123&quot;. Give the user up to 4 attempts using a
# loop.
# If they type &quot;exit&quot;, stop the program immediately using break.
# If they get it right, print &quot;Identity verified!&quot; and break.
# If they run out of tries, print &quot;Account locked for security.&quot;
old_password = "password123"
chances = 1
for i in range(1,5):
    password = int(input("enter the old password:"))
    if password == "exit":
        print("pgs stoped")
        break
    elif password== old_password:
        print("Identity verified")
        break
    else:
        chances+=1
if chances<4:
    print("Account locked for security")