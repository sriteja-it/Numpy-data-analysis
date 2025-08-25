#1D
import numpy as np
n = np.array([1,2,3,4,5,6])
print("iterating array......")
for a in n:
    print(a)
res=np.array_split(n,2)
print("\n After splitting i.e return two arrays")
for a in res:
    print(a)
