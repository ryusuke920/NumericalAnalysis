import math
import numpy as np
from matplotlib import pyplot

x = np.linspace(0, 2 * math.pi, 100) 
y = np.sin(x)
pyplot.plot(x, y)
pyplot.show()