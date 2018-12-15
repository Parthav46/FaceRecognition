import matplotlib.image as matimage
import matplotlib.pyplot as plt
from scaling import resize
from PCA import PCA

image = matimage.imread("temp.jpg")
# plt.imshow(image)
# plt.show()
finalim = resize(image, (50, 50))
pca = PCA()
pca.add(finalim)
pca.add(finalim)
pca.add(finalim)
pca.print()
# plt.imshow(finalim)
# plt.show()
