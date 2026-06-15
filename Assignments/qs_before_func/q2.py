# Question 2: Password Validator using a while loop
# Exercise: Automated Security Gatekeeper
# You are working as a Junior Security Software Engineer for a corporate data center. The company
# requires a secure gateway script for a terminal interface. The system must validate a user&#39;s
# password before granting them access to the secure server environment.
# To prevent automated &quot;brute-force&quot; hacking attacks (where a computer program quickly guesses
# thousands of passwords), the system must have a strict limit on the number of consecutive
# incorrect entries allowed.
# Problem Specification
# Write a Python program that acts as an authentication gateway. The system must meet the
# following technical requirements:
# 1. Predefined Credentials: The system should have a fixed master password stored securely
# in a variable (&quot;Luminar@2026&quot;).
# 2. Controlled Repetition: Use a while loop to repeatedly prompt the user to input their
# password.
# 3. Dynamic Feedback: Every time the user is prompted, the terminal must display the current
# attempt number out of the maximum allowed attempts (e.g., Attempt 1/3, Attempt 2/3).
# 4. Immediate Exit: If the user enters the correct password, the system should immediately
# print a success message (&quot;Access Granted! Welcome to your environment.&quot;) and terminate
# the loop right away.
# 5. Clean Lockout Logic: If the user fails all 3 attempts, the system must trigger a security
# lockdown and print an error message (&quot;Account locked. Too many failed attempts.&quot;).
# Expected Input/Output Behaviors
# example
# Enter password (Attempt 1/3): password123
# Incorrect password.
# Enter password (Attempt 2/3): Luminar@2026
#
# Access Granted! Welcome to your environment.
attempts =  0
while attempts<3:
    password = input(f"Enter the password(Attempts{attempts+1}):")
    if password =="Luminar@2026":
        print("Access Granted! Welcome to your environment.")
        break
    else:
        print("Incorrect password.")
    attempts+=1
if attempts == 3:
    print("Account locked. Too many failed attempts.")