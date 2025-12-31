import matplotlib.pyplot as plt

import numpy as np

xpoints = np.array([0,6]) #takes all points between 0 to 6

ypoints = np.array([0,25])

plt.plot(xpoints , ypoints , marker='o' , color='b') 

plt.title("line graph")
plt.xlabel("x-axis")
plt.ylabel("y-label")

#show grid
plt.grid(True)

plt.show()

