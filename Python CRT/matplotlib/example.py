import matplotlib as mp
#version
print(mp.__version__)
print(mp.__version_info__)
import matplotlib.pyplot as plt
import numpy as np
A=np.array([1,2,3,4])
B=np.array([2,4,6,8])
plt.plot(A,B,marker='D',color='g')
plt.show()