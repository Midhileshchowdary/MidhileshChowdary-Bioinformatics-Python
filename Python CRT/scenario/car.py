import numpy as np
mileage=np.array([15.2,16.5,14.8,15.9,16.2,15.5])
count=0
for x in mileage:
    if x<15:
        index=mileage[x]+1
print(index)