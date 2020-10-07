#Py MatPlotLib

import numpy as np
import matplotlib.pyplot as plt
from pylab import show

x = np.arange(0,5,0.01)
y = np.sin(x)
plt.plot(x,y)
show()