import numpy as np


def resize(test_image, dimensions):
    if len(test_image.shape) == 3:
        test_image = test_image[:, :, 0]
    if test_image.shape[0] < dimensions[0]:
        test_image = _expand(test_image, (dimensions[0], test_image.shape[1]))
    elif test_image.shape[0] > dimensions[0]:
        test_image = _compress(test_image, (dimensions[0], test_image.shape[1]))
    if test_image.shape[1] < dimensions[1]:
        test_image = _expand(test_image.transpose(), (dimensions[1], dimensions[0]))
    elif test_image.shape[1] > dimensions[1]:
        test_image = _compress(test_image.transpose(), (dimensions[1], dimensions[0]))
    return test_image.transpose()


def _expand(test_image, dimensions):

    # Purpose of this function is to expand a numpy array to a desired height
    # Note:
    # - Function only works to expand height dimension enter transpose image and then
    #   transpose the answer to expand width
    # - The function only works if the desired height is larger than the actual height

    (height, width) = dimensions
    actual_height, actual_width = test_image.shape[:2]
    if actual_height * actual_width >= height * width:
        return np.zeros([1, 1])
    factor = actual_height / (height - actual_height)
    counter = 0

    j = 1
    i = 1
    final_image = test_image[0, :]
    while i < height:
        if j < actual_height:
            if counter <= factor:
                final_image = np.vstack([final_image, test_image[j, :]])
                j += 1
                counter += 1
            else:
                fill = [((int(test_image[j-1, i]) + int(test_image[j, i]))//2) for i in range(actual_width)]
                final_image = np.vstack([final_image, fill])
                counter -= factor
            i += 1
        else:
            filling = np.zeros([1, actual_width])
            tempbot = (height-i-1)//2
            temptop = height-tempbot-i
            for i in range(temptop):
                final_image = np.vstack([filling, final_image])
            for i in range(tempbot):
                final_image = np.vstack([final_image, filling])
            i = height
    return final_image


def _compress(test_image, dimensions):

    # Purpose of this function is to compress a numpy array to a desired height
    # Note:
    # - Function only works to compress height dimension enter transpose image and then
    #   transpose the answer to compress width
    # - The function only works if the desired height is smaller than the actual height

    (height, width) = dimensions
    actual_height, actual_width = test_image.shape[:2]
    if actual_height * actual_width < height * width:
        return np.zeros([1, 1])
    factor = height / (actual_height - height)
    counter = 0

    j = 1
    i = 1
    final_image = test_image[0, :]
    while i < height:
        if j < actual_height:
            if counter <= factor:
                final_image = np.vstack([final_image, test_image[j, :]])
                i += 1
                counter += 1
            else:
                counter -= factor
            j += 1
        else:
            filling = np.zeros([1, actual_width])
            tempbot = (height-i-1)//2
            temptop = height-tempbot-i
            for i in range(temptop):
                final_image = np.vstack([filling, final_image])
            for i in range(tempbot):
                final_image = np.vstack([final_image, filling])
            i = height
    return final_image
