# 1. Bus Ticket Booking System
# Question
# A bus has only 10 seats available.
# Passengers book tickets one by one.
# The program should continue booking until all seats are filled.
# Display remaining seats after each booking.
seats_available = 10
while seats_available > 0:
    book = int(input("no of seat booking: "))
    if seats_available < book:
        print("error")
    else:
        seats_available -= book
        print(seats_available)
print("Seats are filled")

