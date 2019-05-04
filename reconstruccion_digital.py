import numpy as np 
import matplotlib.pyplot as pl
from PIL import Image ###permite abrir y manipular imagenes
from proptfr import proptfr



M = 768 # numero de pixeles del modulador
N = 768
dx = 19e-6 # tamano del modulador
LX = M*dx
LY = M*dx
x = np.linspace(-LX/2,(LX/2)-dx, M) # dominio espacial modulador
y = x
l_onda = 514e-9 # longitud de onda
k = 2+np.pi/l_onda # numero de onda
w = 100*dx
z = 0.8
xx = np.where(abs(x)<= w , 1, 0) # funcion rectangulo de ancho 2w
X , Y = np.meshgrid(xx ,xx)
entrada = X*Y #funcion rectangulo 
# entrada = imagen_pix
fdifraccion = proptfr()
difraccion = fdifraccion.proptf(entrada, l_onda, z)
ref = np.exp(1j*k*z)*np.ones([M, M], dtype = int) 
holograma = (ref+difraccion)**2
holoint = abs(holograma**2)
holoint = holoint/np.max(holoint)
holorecons = fdifraccion.proptf(ref*holoint, l_onda, z)
#pl.imshow(abs(difraccion)**2)
#pl.show()
# trans = np.fft.fftshift(entrada)
# transf = np.fft.fft2(trans)

pl.subplot(1,4,1)
pl.imshow(entrada, cmap = 'gray')
pl.title('Senal de Entrada')
pl.subplot(1,4,2)
pl.imshow(abs((difraccion)**2), cmap = 'gray')
pl.title('Difraccion')
pl.subplot(1,4,3)
pl.imshow(abs(holograma)**2, cmap = 'gray')
pl.title('Holograma')
pl.subplot(1,4,4)
pl.imshow(abs(holorecons.conjugate())**2, cmap = 'gray')
pl.title('Reconstruccion')
pl.show()

