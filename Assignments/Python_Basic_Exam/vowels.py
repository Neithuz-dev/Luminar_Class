# The Vowel and Consonant Counter
# Write a program that asks the user to enter a sentence. The program must count and print the
# total number of vowels AND the total number of consonants in that sentence.
#  Vowels are: a, e, i, o, u (case-insensitive).
#  Consonants are all other letters of the alphabet.
#  Important: Do not count spaces, numbers, or punctuation marks (like !, ., or ?) as
# consonants.
# Example:
#  Input: Python 3.0!
#  Output: * Total Vowels: 1 (the &#39;o&#39;)
# o Total Consonants: 5 (P, y, t, h, n)
# o (Note: Spaces, &#39;3&#39;, &#39;0&#39;, &#39;.&#39;, and &#39;!&#39; are completely ignored).

string = "Python3.0"
vowels_count = 0
vowel_char = ""
consonants = 0
consonants_char = []

for char in string:
    if char.isalpha():
        if char in "aeiou":
            vowels_count +=1
            vowel_char += char
        else:
            consonants +=1
            consonants_char+= char
print("Total Vowels:",vowels_count,f"({vowel_char})")
print("Total Consonants:",consonants,f"({consonants_char})")