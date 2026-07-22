# Question 1: Find Common Elements Between Two Lists
# Question
#
# Write a function that takes two lists and returns a list containing the common elements without duplicates.
#
# Example
#
# Input
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
#
# Output
#
# [3, 4, 5]

def common(list1,list2):
    new_ls=[]
    for i in list1:
        if i  in list2:
            new_ls.append(i)
        else:
            pass
    return new_ls
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

print(common(list1,list2))