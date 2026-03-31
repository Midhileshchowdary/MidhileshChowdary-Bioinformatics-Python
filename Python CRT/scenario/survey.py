import numpy as np
ratings=np.array([4,3,5,2,5,3,4,5,1])
count=0
for x in ratings:
    if (x==5):
        count+=1
print(count)