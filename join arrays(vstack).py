import numpy as np
n1=np.array([2,638,67,33,31,42,37])
n2=np.array([43,65,10,93,92,10,19])
print("Iterating array")
for a in n2:
    print(a)
res=np.vstack((n1,n2))
print("\n After stacking along columns:\n",res)
