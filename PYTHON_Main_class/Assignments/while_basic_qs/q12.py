# 12. Game Coin Collection
# Question
# In a mobile game, a player collects coins.
# The game continues until the player reaches 500 coins
total_coins = 0
while total_coins < 500:
    coins = int(input("No of coins collected: "))
    total_coins+=coins
    if total_coins >500:
        print("Error")
    elif total_coins==500:
        print("Game over")
