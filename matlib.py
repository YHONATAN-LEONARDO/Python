import numpy as np
import matplotlib.pyplot as plt 
x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])

coe = np.polyfit(x,y,1)

pendiente, intercepto = coe

y_predi  = pendiente * x  +  intercepto
plt.scatter(x,y)
