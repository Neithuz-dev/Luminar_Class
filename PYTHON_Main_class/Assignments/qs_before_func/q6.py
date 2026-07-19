# Question 6:The Robot Maze Game
# The Story
# Imagine you are playing a video game with a small robot. The robot has to walk through a hallway
# with 15 numbered rooms (Room 1 to Room 15).
# As the robot walks into each room, it shouts out the room number. But there are two special rules
# in this maze:
#
# 1. The Jump Rule (Room 5): When the robot gets to Room 5, it steps on a magic button.
# The button jumps the robot straight into Room 6. Because it jumps, the robot does not
# shout out the number 5.
# 2. The Stop Rule (Room 12): When the robot reaches Room 12, it finds the final exit door.
# The game is over! The robot stops completely and does not go to rooms 13, 14, or 15.
for i in range(1,16):
    if i == 5:
        print("Skip")
        continue
    elif i ==12:
        print("Game over")
        break
    else:
        print("shouts out ",i)