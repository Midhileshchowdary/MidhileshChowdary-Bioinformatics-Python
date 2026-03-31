import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
colors=np.array([10,20,30,40])
plt.scatter(x,y,c=colors,cmap='viridis')
plt.show()

