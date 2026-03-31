import numpy as np
import matplotlib.pyplot as plt
#plot1:
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(2,3,1)
plt.title("Plot-1")
plt.plot(x,y)

#plot2:
x=np.array([0,1,2,3])
y=np.array([55,20,50,40])
plt.subplot(2,3,2)
plt.title("Plot-2")
plt.plot(x,y)


#plot3:
x=np.array([0,1,2,3])
y=np.array([3,7,9,11])
plt.subplot(2,3,3)
plt.title("Plot-3")
plt.plot(x,y)

#plot4:
x=np.array([0,1,2,3])
y=np.array([3,12,14,10])
plt.subplot(2,3,4)
plt.title("Plot-4")
plt.plot(x,y)


#plot5:
x=np.array([0,1,2,3])
y=np.array([3,15,16,10])
plt.subplot(2,3,5)
plt.title("Plot-5")
plt.plot(x,y)

#plot6:
x=np.array([0,1,2,3])
y=np.array([3,18,17,10])
plt.subplot(2,3,6)
plt.title("Plot-6")
plt.plot(x,y)
plt.show()