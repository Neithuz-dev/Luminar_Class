# Question 2: Password Validator using a while loop
# Exercise: Automated Security Gatekeeper
# You are working as a Junior Security Software Engineer for a corporate data center. The company requires a secure gateway script for a terminal interface. The system must validate a user's password before granting them access to the secure server environment.
# To prevent automated "brute-force" hacking attacks (where a computer program quickly guesses thousands of passwords), the system must have a strict limit on the number of consecutive incorrect entries allowed.
# Problem Specification
# Write a Python program that acts as an authentication gateway. The system must meet the following technical requirements:
# 1.	Predefined Credentials: The system should have a fixed master password stored securely in a variable ("Luminar@2026").
# 2.	Controlled Repetition: Use a while loop to repeatedly prompt the user to input their password.
# 3.	Dynamic Feedback: Every time the user is prompted, the terminal must display the current attempt number out of the maximum allowed attempts (e.g., Attempt 1/3, Attempt 2/3).
# 4.	Immediate Exit: If the user enters the correct password, the system should immediately print a success message ("Access Granted! Welcome to your environment.") and terminate the loop right away.
# 5.	Clean Lockout Logic: If the user fails all 3 attempts, the system must trigger a security lockdown and print an error message ("Account locked. Too many failed attempts.").
# Expected Input/Output Behaviors
# example
# Enter password (Attempt 1/3): password123
# Incorrect password.
# Enter password (Attempt 2/3): Luminar@2026
# Access Granted! Welcome to your environment.
attempts_ = 1
while attempts_ <=3 :
    password = input(f"enter the password{attempts_}/3:")
    if password =="Luminar@2026":
        print("Access Granted! Welcome to your environment.")
        break
    else:
        print("Incorrect password.")
    attempts_ += 1
if attempts_ >3:
        print("Account locked. Too many failed attempts.")
