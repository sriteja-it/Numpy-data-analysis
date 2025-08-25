import numpy as np
n= np.array([1,2,3,4,5])
print("Iterating arrays")
for a in n:
    print(a)
print("sorted\n",np.sort(n))
s=np.array(["java","android","os","python"])
print('\n Iterating array;\n')
for i in s:
    print(i)
res=np.sort(s)
print("\nsorted array",res)