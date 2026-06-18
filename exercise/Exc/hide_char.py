message = "secret password"
char_hide = "s"
result = ""
for char in message:
    if char.lower() == char_hide.lower():
        result += "*"
    else:
        result += char

print(result)