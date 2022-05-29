from PIL import Image
import numpy as np
import scipy

filename = "dog.png"
img = Image.open(filename)
#img.show()

pixel = img.getpixel((0,0))
print (pixel)

im = Image.open(filename)
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((0,0))
print(r, g, b)

im = Image.open('dog.png')
im_matrix = np.array(im)
print(im_matrix[0][0])


import imageio
im = imageio.imread('dog.png', pilmode='RGB')
print(im.shape)
color = tuple(im[0][0])
r, g, b = color
print(r, g, b)
