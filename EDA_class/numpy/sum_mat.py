import numpy as  np
a1 = np.array([3,4,5,6,7])
print(np.sum(a1))

m1 = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
print(np.sum(m1))
print(np.sum(m1,axis=1))

print(np.sort(m1,axis=0))

print(np.max(a1))
print(np.max(m1,axis=1))