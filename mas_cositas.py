import matplotlib.pyplot as plt
from skimage import io
import numpy as np

lena_rgb=io.imread("dog.png")# imread lee las imagenes con los pixeles codificados como enteros 
# en el rango 0-255. Por eso la convertimos a flotante y en el rango 0-1

print("- Dimensiones de la imagen:")
print(lena_rgb.shape)
plt.imshow(lena_rgb,cmap="gray",vmin=0,vmax=255)

# Ejercicio: Convertir la imagen de lena color a escala de grises

h,w=lena_rgb.shape # obtenemos el tamaño de la imagen original

lena_gris=np.zeros((h,w)) # creamos una matriz donde generar la imagen

for i in range(h):
    for j in range(w):
        if i == 0:
            if j == 0:
                print (lena_rgb[i][j])
        #IMPLEMENTAR
        # calcular el promedio de los canales r,g,b del pixel i,j con la imagen original
        # guardar ese promedio en el pixel i,j de la imagen generada

plt.imshow(lena_gris) 

#plt.show()