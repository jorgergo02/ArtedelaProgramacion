import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
import math
from convolution import convolution
from sobel import metodo_sobel
from Simple import metodo_simple
from gaussian_smoothing import gaussian_blur
from metodo_MexicanHat import metodo_MexHat
from line_detection import line_det
import urllib.request as urllib

#Lee la imagen desde el internet y lo convierte a una matriz
resp = urllib.urlopen("https://i.pinimg.com/originals/2d/cb/2f/2dcb2f2393ef73477520028089b9ed1f.jpg")
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)

#Agrega un padding de 50 pixeles a la imagen de todos los lados
def pad_with(vector, pad_width, iaxis, kwargs):
        pad_value = kwargs.get('padder', 10)
        vector[:pad_width[0]] = pad_value
        vector[-pad_width[1]:] = pad_value

image = np.pad(image, 50, pad_with, padder=0)

size=int(input("Longitud del kernel que se desea: "))
if size % 2 == 0:
    size = size + 1

#Metodo_Simple
metodo_simple(image, size, verbose=True)

#Metodo_Sobel
metodo_sobel(image, size, verbose=True)

#Gaussian_Blur
gaussian_blur(image, size, 4, verbose=True)

#Mexican_Hat
metodo_MexHat(image, size, 4, verbose=True)

#Line_Detection
line_det(image, size, verbose=True)

