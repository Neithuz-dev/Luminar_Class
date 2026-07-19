import numpy as np
a1 = np.array(([4,5,6,7,8,9,10,1,2,3]))
print(a1[:8:2])
print(a1[-1:7:-1])
print("-"*100)
a2 = np.array([
    [2,3,4,5,7],
    [6,1,8,9,4],
    [8,3,6,9,2],
    [4,9,1,7,8]
])
print(a2[2:,:3])
print("-"*100)
print(a2[1:3,2:4])
print("-"*100)
print(a2[:4])