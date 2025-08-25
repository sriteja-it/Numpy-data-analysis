import numpy as np
n = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("iterating array......")
for a in n:
    print(a)
res=np.array_split(n,2)
print("\n After splitting indivitually.....")
print("\n array1=",res[0])
print("\narray2=",res[1])