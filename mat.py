# data m1
"""
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("scottish_hills.csv")
x=data.Height
y=data.Latitude

plt.scatter(x,y)
plt.savefig('my_hills1.png')
#plt.plot(x,y)
plt.show()







#data m2
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("scottish_hills.csv")

x = dataframe.Height
y = dataframe.Latitude

# Change the default figure size
plt.figure(figsize=(10,10))

# Change the default marker for the scatter from circles to x's
plt.scatter(x, y, marker='x',color='r',label='Mr. Kang')


# Add x and y lables, and set their font size
plt.xlabel("Height (m)",color='b', fontsize=20)
plt.ylabel("Latitude", color='g',fontsize=20)
plt.title("Height & Latitude",fontsize=28)
plt.legend()
# Set the font size of the number lables on the axes
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.savefig("my_hills2.png")









#pandas, numpy, matplotlib
# importing libraries
import matplotlib.pyplot as plt
import numpy as np
import math
  
# Get the angles from 0 to 2 pie (360 degree) in narray object
X = np.arange(0, math.pi*2, 0.05)
  
# Using built-in trigonometric function we can directly plot
# the given cosine wave for the given angles
Y1 = np.sin(X)
Y2 = np.cos(X)
Y3 = np.tan(X)
Y4 = np.tanh(X)
  
# Initialise the subplot function using number of rows and columns
figure, axis = plt.subplots(2, 2)
  
# For Sine Function
axis[0, 0].plot(X, Y1)
axis[0, 0].set_title("Sine Function")
  
# For Cosine Function
axis[0, 1].plot(X, Y2)
axis[0, 1].set_title("Cosine Function")
  
# For Tangent Function
axis[1, 0].plot(X, Y3)
axis[1, 0].set_title("Tangent Function")
  
# For Tanh Function
axis[1, 1].plot(X, Y4)
axis[1, 1].set_title("Tanh Function")
  
# Combine all the operations and display
plt.show()

"""






#plot sin & cos
# Importing libraries
import matplotlib.pyplot as plt
import numpy as np
import math
  
# Using Numpy to create an array X
X = np.arange(0, math.pi*2, 0.05)
  
# Assign variables to the y axis part of the curve
y = np.sin(X)
z = np.cos(X)
  
# Plotting both the curves simultaneously
plt.plot(X, y, color='r', label='sin',linestyle='dashed')
plt.plot(X, z, color='g', label='cos',linestyle='solid')
  
# Naming the x-axis, y-axis and the whole graph
plt.xlabel("Angle")
plt.ylabel("Magnitude")
plt.title("Sine and Cosine functions")
  
# Adding legend, which helps us recognize the curve according to it's color
plt.legend()
  
# To load the display window
plt.show()