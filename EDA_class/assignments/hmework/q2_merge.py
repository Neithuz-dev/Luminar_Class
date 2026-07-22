# Question 2: Merge Two Dictionaries
# Question
#
# Write a function to merge two dictionaries. If a key exists in both dictionaries, add their values.
#
# Example
#
# Input
#
# d1 = {"A":10,"B":20,"C":30}
# d2 = {"B":15,"C":5,"D":40}
#
# Output
#
# {'A':10,'B':35,'C':35,'D':40}

def merge(d1,d2):
    new_d ={}
    for i,v in d1.items():
        if i not in d2:
            new_d[i]=v
        else:
            new_d[i]= v+d2[i]
    for i ,v in d2.items():
        if i not in d1:
            new_d [i]=v
    return  new_d


d1 = {"A":10,"B":20,"C":30}
d2 = {"B":15,"C":5,"D":40}
print(merge(d1,d2))