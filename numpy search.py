import numpy as np
n = np.array([1,2,3,4,5,43,62])
print("Iterating\n")
for a in n:
    print(a)
res=np.where(n==3)
print("\n element 43 found in array  indexing")
print(res)
