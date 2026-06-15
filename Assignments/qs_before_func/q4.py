# Question 4: Exercise: The Hidden Treasure Number
# Imagine you are playing a treasure hunt game. The game master tells you that a secret treasure
# number is hidden inside a box of numbered cards.
# The cards in the box start at number 100 and go up to number 200 (arranged in order: 100, 101,
# 102...).
# To find the treasure card, it must pass a double magic test:
# 1. It must be perfectly divisible by 7 (leaving a remainder of 0).
# 2. It must also be perfectly divisible by 9 (leaving a remainder of 0).
# Because you want to win the game as fast as possible, you will look at the cards one by one
# starting from 100. The very moment you find a card that passes both tests, you will yell out the
# number and stop looking through the rest of the box.
# Your Task
# Write a simple Python program to find this treasure number. Your code must follow these steps:
# 1. The Setup: Use a loop to check numbers from 100 up to 200.
# 2. The Condition: Check if the current number can be divided by both 7 and 9 with no
# remainder left over.
#
# 3. The Stop: As soon as you find that first correct number, print it on the screen and break
# (stop) the loop immediately.
# Expected Output
# When you run your program, it should only print the one secret number you found first:
#
# The secret treasure number is: 126
for i in range(100,201):
    if i % 7 == 0 and i % 9==0:
        current_num = i
        print(f"Found the number {current_num}")
        break

