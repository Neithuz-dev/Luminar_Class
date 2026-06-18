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