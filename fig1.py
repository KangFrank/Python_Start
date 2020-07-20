import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,10,0.1)
y=x/(1+x)
plt.plot(x,y)
plt.show()
