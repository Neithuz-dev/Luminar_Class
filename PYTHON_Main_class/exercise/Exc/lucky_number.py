# Guess the Secret Lucky Number!
# Imagine a friend thinks of a secret lucky number between 1 and 10. The secret number is 7.
# Your friend says: "I will give you exactly 3 chances to guess my secret number. If you guess it, you win! But if you guess wrong 3 times, you lose the game."
# Your Task
# Write a simple Python program for this game. Your code must follow these rules:
# 1.	The Setup: Create a secret number variable and set it to 7.
# 2.	The Loop: Use a loop to give the player 3 tries to guess.
# 3.	The Win: If the player guesses 7, print a happy message like "You win!" and stop the loop immediately using break.
# 4.	The Loss: If the player uses all 3 tries and never guesses the right number, print "Game Over!".
sec_num = 7
tries = 0
while tries <3:
    num = int(input(f"Guessed number{tries+1}/3: "))
    if num ==sec_num:
        print("You win!")
        break
    else:
        print("Wrong Guess")
        tries+=1
if tries == 3:
    print("Game Over!")