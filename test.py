import os
import matplotlib.image as matimage
import matplotlib.pyplot as plt
import numpy as np
from scaling import compress

image = matimage.imread("temp.jpg")
plt.imshow(image)
plt.show()
compimage = compress(image, (60, 226))
finalim = compress(compimage.transpose(), (60, 60)).transpose()
plt.imshow(finalim)
plt.show()
