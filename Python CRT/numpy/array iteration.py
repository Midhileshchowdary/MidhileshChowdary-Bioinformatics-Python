#array iteration 1d 
import numpy as np
arr=np.array([1,2,3])
for x in arr:
    print(x)

#array iteration 2d 
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
for x in arr:
    print(x)

#array iteration 3d 
import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
    print(x)
print(arr[0,1:])