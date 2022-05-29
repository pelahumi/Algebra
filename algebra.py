import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from PIL import Image

foto = np.ones((100,100,3), np.uint8)

def diagonal_principal(foto):
    for i in foto:
        foto[i] = foto[i] * [255, 0, 0]
    return foto
foto = [5, 56, 20] * foto
m = Image.fromarray(foto)
m.save("1.png")