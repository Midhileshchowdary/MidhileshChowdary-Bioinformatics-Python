#write  py prog to creata a one dimensional array with 15 elements and reshape it into 2d array of with 3 rows and 5 columns
#5 rows and 3 columns and print dimensions of it
#reshape the same array into 3d array with 5 rows and 3 columns with 1 element in each column
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
newarr=arr.reshape(5,3)
print(newarr)
newarr2=arr.reshape(3,5)
print(newarr2)
newarr3=arr.reshape(3,5,1)
print(newarr3)