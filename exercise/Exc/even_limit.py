# Sum of Even Numbers with a Stop Limit
# Problem: Write a program that asks a user for a starting number. Run a while loop that keeps increasing that number by 1.
# If the number is odd, skip it using continue.
# Add up all the even numbers together.
# If the running sum of the even numbers goes over 100, stop the loop completely using break.
start_num = int(input("enter the number:"))
sum = 0
while sum <=100:
    if start_num%2==0:
        sum+=start_num
        start_num += 1

    else:
        start_num += 1
        continue
    if sum >100:
            print(sum)
            break
