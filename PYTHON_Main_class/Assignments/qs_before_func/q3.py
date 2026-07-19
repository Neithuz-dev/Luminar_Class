# Question 3: The Automated Voucher Code Generator (for loop dominant)
# Scenario: An institute wants to generate safe, readable discount voucher codes for a student
# batch. The code must look at a raw string, convert it to uppercase, ignore vowels (to prevent
# accidental bad words), and stop generating if a symbol is detected.
# The Problem:
# Take a raw string like &quot;lum-inar2026&quot;.
# 1. Convert it to uppercase.
# 2. Loop through each character using a for loop.
# 3. If the character is a hyphen -, skip it using continue.
# 4. If the character is a digit, stop the loop entirely using break because voucher prefixes shouldn&#39;t
# have numbers.
# 5. If the character is a vowel (A, E, I, O, U), skip it.
# 6. Otherwise, add it to the final voucher string.
word = "lum-inar2026"
word = word.upper()
voucher = ""
for ch in word:
    if ch.isdigit():
        break
    elif ch=="-":
         continue
    elif ch in "AEIOU":
         continue
    else:
         voucher+=ch
print(voucher)


