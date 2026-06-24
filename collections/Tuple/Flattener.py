# Concept: Unpacking internal tuples using nested loops and appending them to a list before converting the final collection back into a single tuple.
#
# input:
# nestedtuple = ((1, 2), (3, 4), (5, 6))
# output:
# # newtuple = (1,2,3,4,5,6)

nested = ((1,2),(3,4),(5,6))
new = ()
for i in nested:
    if i not in new:
        new+=i
print(new)