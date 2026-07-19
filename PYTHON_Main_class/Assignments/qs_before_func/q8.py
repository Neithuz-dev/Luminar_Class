# Question 8
# The Virtual Piggy Bank (Target Savings)
# Problem: Write a program for a child&#39;s piggy bank. The child wants to save exactly $20. Write a
# loop that keeps asking them to deposit money.
# If they try to deposit a negative amount or $0, ignore it using continue.
# Keep track of the total balance. As soon as the total balance hits or exceeds $20, print a
# celebratory message and stop the loop using break.
save = 0
while True:
    money = int(input("enter the amount: "))
    if money <=0:
        continue
    save += money
    if save >=20:
        print("Saved $20")
        break

