import matplotlib.pyplot as plt
import numpy as np
x=np.array([35,25,25,15])
mylabels=['Apples','Banana','Cherries','Dates']
myexplode=[0.1,0,0,0]
plt.pie(x,labels= mylabels,startangle=180,explode=myexplode,shadow=True)
plt.legend(title="Four Fruits : ")
plt.show()