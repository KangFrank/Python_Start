#numpytest
#!/usr/env/python3
#-*-coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

"""
img=plt.imread("11.jpg")
plt.imshow(img)
"""

x=np.arange(0,3*np.pi,0.1)
y=np.sin(2*x)
y1=np.cos(x)

plt.subplot(2,1,1)
plt.title("Demo")
plt.ylabel("y-axis")
plt.plot(x,y)


plt.subplot(2,1,2)
plt.title("Demo con")
plt.xlabel("x-axis")

plt.plot(x,y1)

plt.show()
