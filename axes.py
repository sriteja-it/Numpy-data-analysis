import numpy as np
n=np.array([[1,2,3],[59,84,35],[78,95,5]])
print("iterating the array:\n")
for i in n:
    print(i)
print("\n minimum value=",n.min())
print("\n minimum value with (vertical axes) =",n.min(axis=0))
print("\n minimum value with (horizontal axes) =",n.min(axis=1))#max
