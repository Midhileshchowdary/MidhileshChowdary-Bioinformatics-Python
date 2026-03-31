import numpy as np
scores=np.array([45,67,89,76,55])
count=0
for x in scores:
    if (x>60):
        count+=1
print(count)