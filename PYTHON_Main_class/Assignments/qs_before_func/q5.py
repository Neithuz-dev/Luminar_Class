# Question 5: The Magic Odd-Box Piggy Bank
# Imagine you have a smart electronic piggy bank called the Magic Odd-Box. This piggy bank only
# wants to collect positive odd numbers (like 1, 3, 5, 7...).
# You start dropping numbered coins into the slot one by one. The piggy bank has a built-in
# computer that reads each coin and follows these strict rules:
# 1. Negative Numbers: If you drop a negative number (like -5), the box rejects it. It prints
# &quot;Skipping negative number...&quot; and waits for the next coin.
# 2. Even Numbers: If you drop an even number (like 4 or 10), the box rejects it too. It prints
# &quot;Skipping even number...&quot; and waits for the next coin.
# 3. The Stop Button: If you drop a coin with the number 0, the machine turns off completely.
# 4. The Success Rule: If the number is positive and odd, the box says &quot;Added!&quot;, drops it into
# the total pile, and adds it to the sum.
# Your Task
# Write a Python program using a while True loop to simulate this smart piggy bank. Your program
# must:
#  Continuously ask the user for an integer.
#  Use break to stop when 0 is entered.
#  Use continue to instantly skip negative and even numbers without adding them.
#  Keep a running total of the valid numbers and print the final sum at the end.
total_sum = 0
while True:
    coin = int(input("Enter the coin number"))
    if coin == 0:
        print("The machine turns off completely.")
        break
    elif coin <0:
        print("Skipping negative number...")
        continue
    elif coin % 2!= 0 and coin >0:
        print("Added")
        total_sum+=coin
    else:
        print("Skipping the even number....")
        continue
    print("Bank Balance:",total_sum)
