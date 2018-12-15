import numpy as np


class PCA:
    image_matrix = None
    initial = False

    def add(self, image):
        line_image = image.ravel()
        if self.image_matrix is None:
            self.image_matrix = np.zeros([2, line_image.shape[0]])
            np.vstack((self.image_matrix, line_image))
            self.initial = True
        else:
            np.vstack((self.image_matrix, line_image))
            if self.initial:
                self.image_matrix = np.vsplit(self.image_matrix, 2)
                self.initial = False

    def print(self):
        print(self.image_matrix)
