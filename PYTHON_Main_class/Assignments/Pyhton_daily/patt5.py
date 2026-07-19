# Q12. Letter Pattern
# Write a Python program to print the following pattern, where each row adds one more letter of the word "python":
# p
# py
# pyt
# pyth
# pytho
# python

text = "python"
length =len(text)

for i in range(length):
  for j in range(i+1):
      print(text[j],end = " ")
  print()
