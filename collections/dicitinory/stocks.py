# Product Stock Tracker
# Question
# A shop stores product quantities in a dictionary.
# Find products whose stock is less than 10.
# Input
# {
#     "Mobile":15,
#     "Laptop":5,
#     "Tablet":8,
#     "Mouse":20
# }
# Output
# Laptop
# Tablet

text = {"Mobile":15,
    "Laptop":5,
    "Tablet":8,
    "Mouse":20}
def stock_count(text):
    for item,no in text.items():
        if no <10:
            print(item)

stock_count(text)

