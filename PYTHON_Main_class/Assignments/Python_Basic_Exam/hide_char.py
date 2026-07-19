# Character Masking (Censorship)
# Problem Description: Write a program that asks the user for a secret message and a specific
# character they want to hide. The program should loop through the message and replace every
# occurrence of that character with an asterisk (*).
# Example:
#  Input Message: secret password123
#  Character to hide: s
#  Output: *ecret pa**word123

message = "secret password"
char_hide = "s"
result = ""
for char in message:
    if char.lower() == char_hide.lower():
        result += "*"
    else:
        result += char

print(result)