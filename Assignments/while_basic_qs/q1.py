# 1. Bus Ticket Booking System
# Question
# A bus has only 10 seats available.
# Passengers book tickets one by one.
# The program should continue booking until all seats are filled.
# Display remaining seats after each booking.
book = int(input("no of seat booking: "))
seats_available = 10
while book<seats_available:
    seats_available -= book
    print(seats_available)
    book = int(input("no of seat booking: "))
print("Seats are filled")
