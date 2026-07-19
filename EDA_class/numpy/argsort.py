import numpy as np
a1 = np.array([4,5,6,7,8,9])
# print(np.argsort(a1))
# print(np.argmax(a1))
print(np.where(a1>5))

# a2 = np.array([
#     [3,9,5,2],
#     [2,9,5,6],
#     [5,8,6,2]
# ])
# print(np.argsort(a2,axis=0))
# print(np.argmax(a2))

marks = np.array([50,60,30,70,40,68])
cat =np.where(marks>50,"pass","fail")
print(cat)