import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from PIL import Image

foto = np.ones((4,5,3), np.uint8)


def plantilla(foto):
    for i in range(5):
        foto[1,i] = foto[1,i] * [255, 255, 255]
        foto[3,i] = foto[3,i] * [255, 255, 255]

        for j in range(4):
            foto[j,1] = foto[j,1] * [255, 255, 255]
            foto[j,3] = foto[j,3] * [255, 255, 255]

    return foto

def corazon(foto):

    foto[3,0], foto[3,4] = foto[3,0] * [255, 255, 255], foto[3,4] * [255, 255, 255]
    foto[1,1] = foto[1,1] * [255, 255, 255]
    foto[1,3] = foto[1,3] * [255, 255, 255]
    foto[2,2] = foto[2,2] * [255, 255, 255]

    for i in range(len(foto)):
        if foto[i,] == [255,255,255]:
            foto[i] = [255,0,0]
        
    return foto


plantilla(foto)
corazon(foto)
m = Image.fromarray(foto)
m.save("img/1.png")