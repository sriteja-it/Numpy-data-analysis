import numpy as np
n1=np.array([1,2,3,4,5,6])
n2=np.array([7,5,8,3,10,4,11,12,13,14])
print("iteratin array1....")
for a in n1:
    print(a)
print("iteratin array2....")
for a in n2:
    print(a)
diff=np.setdiff1d(n1,n2)
print("\ndiference :",diff)
diff2=np.setdiff1d(n2,n1)
print(diff2)
