import matplotlib.pyplot as plt
import numpy as np
x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,285,290,295,300,315,320,335,3500,365])
plt.plot(x,y)
plt.title("Sports watch data",loc='right')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie burnage")

plt.plot(x,y)
plt.grid(axis='x',color='green',linestyle='--',linewidth=3)
plt.show()