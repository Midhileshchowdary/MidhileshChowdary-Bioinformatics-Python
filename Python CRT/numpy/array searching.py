#searching array: where method is used 
import numpy as np
arr=np.array([1,2,3,4,5,4,4])
x=np.where(arr==4)
print(x)
#finding indexes are even
arr=np.array([1,2,3,4,5,6,7,8])
x=np.where(arr%2==0)
print(x)
#finding indexes are odd
arr=np.array([1,2,3,4,5,6,7,8])
x=np.where(arr%2==1)
print(x)