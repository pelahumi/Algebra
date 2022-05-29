# Convertir una imagen a un array
# Importamos a misc
from scipy import misc


#Importamos matplotlib
import matplotlib.pyplot as plt

# Imagen en escala de grises
gray = misc.face(gray=True)

# Mostramos la imagen
plt.imshow(gray,cmap=plt.cm.gray)
plt.show()
