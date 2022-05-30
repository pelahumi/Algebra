import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from PIL import Image

foto = np.ones((100,100,3), np.uint8)


def pintar(foto):
    for i in range(len(foto)):
        foto[i] = foto[i] * [255, 255, 0]
    
    for i in range(len(foto)//3):
        foto[i] = foto[i] * [1, 0, 0]
        foto[-i] = foto[-i] * [1, 0, 0]
    return foto

pintar(foto)

m = Image.fromarray(foto)
m.save("1.png")