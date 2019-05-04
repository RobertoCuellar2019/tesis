import numpy as np
import matplotlib.pyplot as pl
class proptfr:
   
    def __init__(self):
        print("")

    def proptf(self, entrada, l_onda, z):
        M = 768
        N = 768
        dx = 19e-6
        LX = M*dx
        LY = N*dx
        pi =np.pi
        fx = np.linspace(-1/(2*dx),1/(2*dx)-1/LX, M)
        fy = fx
        FX, FY = np.meshgrid(fx, fy)
        H = np.exp(-1j*pi*l_onda*z*((FX**2)+(FY**2)))
        H = np.fft.fftshift(H)
        U1 = np.fft.fft2(np.fft.fftshift(entrada))
        U2 = H*U1
        salida =np.fft.fftshift(np.fft.ifft2(U2))
        #pl.imshow(abs(np.fft.fftshift(salida))**2)
        #pl.show()
        return (salida)
