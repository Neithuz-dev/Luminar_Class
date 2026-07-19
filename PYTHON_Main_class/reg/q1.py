# import re
# text = "Python is easy to learn."
# print(re.search(r"Python",text.capitalize()))
# import re
#
# text = "I have 3 cats, 5 dogs, and 12 fish."
# print(re.findall(r"\d+",text))

# import re
# text = "Programming"
# vowels = re.findall(r"[aeiou]",text)
# print(vowels)

# import re
# text ="Python is easy"
# print(re.sub(r" ","-",text))

import re
text = "Python Programming Practice Java"
print(re.findall(r"\bP\w+",text))