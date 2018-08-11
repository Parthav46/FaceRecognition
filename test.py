import os
import matplotlib.image as matimage
import matplotlib.pyplot as plt
import numpy as np
from scaling import resize

image = matimage.imread("temp.jpg")
plt.imshow(image)
plt.show()
finalim = resize(image, (50, 50))
plt.imshow(finalim)
plt.show()
