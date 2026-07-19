# Write a Python function to check whether a given string is a Pangram or not. A pangram is a sentence that contains every letter of the English alphabet at least once, regardless of case.
# Example: Input: "The quick brown fox jumps over the lazy dog" Output: "It's a Pangram"
text = "The quick brown fox jumps over the lazy dog"
letters ="abcdefghijklmnopqrstuvwxyz"
str = ""

for char in text.lower():
    if char in letters:
        if char not in str:
            str +=char
if len(str)==26:
    print("Pangarm")
else:
    print("Not a panagram")