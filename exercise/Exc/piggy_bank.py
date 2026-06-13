# The Virtual Piggy Bank (Target Savings)
# Problem: Write a program for a child's piggy bank. The child wants to save exactly $20. Write a loop that keeps asking them to deposit money.
# If they try to deposit a negative amount or $0, ignore it using continue.
# Keep track of the total balance. As soon as the total balance hits or exceeds $20, print a celebratory message and stop the loop using break.
save = 20
bal_ance = 0
for i in range(save):
    depo = int(input("enter the amount: "))
    if depo <=0:
        continue
    bal_ance += depo
    if bal_ance >= save:
        print("Reached Your savings!!!!!!!")
        break


