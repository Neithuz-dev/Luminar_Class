text = input("enter the sentences").lower()
alphabets = "abcdefghijklmnopqrstuvwxyz"

for char in alphabets:
    if char not in text:
        print("not pangram")
        break
else:
    print("Its a pangram")
