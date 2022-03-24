import numpy as np
import cv2
import matplotlib.pyplot as plt
from convolution import convolution
from scipy import signal


def line_det(image, size, verbose=False):
    #Vertical
    vertical_matriz = [[-1,2,-1],
                       [-1,2,-1],
                       [-1,2,-1]]
    matriz=np.array(vertical_matriz)
    new_image_v = convolution(image, matriz)

    if verbose:
        plt.imshow(new_image_v, cmap='gray')
        plt.title("Vertical lines")
        plt.show()

    #Horizontal
    horizontal_matriz = [[-1,-1,-1],
                         [2,  2, 2],
                         [-1,-1,-1]]
    matriz=np.array(horizontal_matriz)
    new_image_h = convolution(image, matriz)

    if verbose:
        plt.imshow(new_image_h, cmap='gray')
        plt.title("Horizontal lines")
        plt.show()
