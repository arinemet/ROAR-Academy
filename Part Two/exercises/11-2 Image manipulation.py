from matplotlib import image
from matplotlib import pyplot as plt
import os
path = os.path.dirname(os.path.abspath(__file__))
filename = path + "/../samples/" + "lenna.bmp"
data = image.imread(filename)
flag = image.imread(path + "/../../united-states-of-america-flag-png-large.png.jpeg")
flag = flag[::4, ::4, :]
plt.imshow(data)
plt.autoscale(False)
plt.imshow(flag)
plt.show()