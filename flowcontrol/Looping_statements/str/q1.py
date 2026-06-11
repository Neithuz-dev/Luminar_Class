# Scenario: In Data Analytics, you often need to filter data based on multiple mathematical conditions. Task: Write a Python program that iterates through numbers from 1 to 50.
# •	For multiples of 3, print "Data" instead of the number.
# •	For multiples of 5, print "Analytics" instead of the number.
# •	For numbers which are multiples of both 3 and 5, print "Data Analytics".
# •	For all other numbers, print the number itself.
for i in range(1,51):
    if i%3==0 and i%5==0:
        print("Data Analytics ")
    elif i%3==0:
        print("Data")
    elif i%5 == 0:
        print("Analytics")
    else:
        print(i)