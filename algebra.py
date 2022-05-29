import numpy as np
from skimage import io
import matplotlib.pyplot as plt

foto1 = np.zeros((4,4), np.uint8)
foto2 = np.ones((4,4), np.uint8)

plt.imshow(foto1)
plt.imshow(foto2)
plt.show()