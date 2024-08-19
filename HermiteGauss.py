import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial, hermite

def HP(n, x):
    """
    Generate the Hermite polynomial H_n(x) using the Rodrigues formula.

    Parameters:
    n (int): The degree of the Hermite polynomial.
    x (float or np.ndarray): The point(s) at which to evaluate the polynomial.

    Returns:
    H_n_x (float or np.ndarray): The value(s) of the Hermite polynomial H_n(x).
    """
    p_monic = hermite(n)
    H_n_x = p_monic(x)

    return H_n_x

class HermiteGaussian:
    def __init__(self,L,
                size, 
                n,
                m,
                w0,
                k,
                z) -> None:
        self.size = size
        self.L = L
        self.w0 = w0
        self.n = n
        self.m = m
        self.k = k
        self.z = z


        x, y = np.linspace(-self.L, self.L, self.size), np.linspace(-self.L, self.L, self.size)
        Y, X = np.meshgrid(x, y)

        if self.z == 0:
            self.HGB = (1/self.w0) * np.sqrt(2/(np.pi * (2 ** (self.m+self.n)) * factorial(self.m) * factorial(self.n))) * HP(self.m, np.sqrt(2)*X/self.w0) * HP(self.n, np.sqrt(2)*Y/self.w0) * np.exp(-(X**2 + Y **2)/self.w0**2)

        else:

            zr = 1/2 * self.k * self.w0 ** 2
            wz = self.w0 * np.sqrt(1 + (z/zr) ** 2)
            Rz = z * (1 + (zr / z) ** 2)

            self.GouyPhase = np.arctan(z/zr)

            self.HGB = (1/wz) * np.sqrt(2/(np.pi * 2 ** (self.m+self.n) * factorial(self.m) * factorial(self.n))) * HP(self.m, np.sqrt(2)*X/wz) * HP(self.n, np.sqrt(2)*Y/wz)*np.exp(-(X**2 + Y **2)/wz**2) * np.exp(-1j * (self.k * z + (self.m + self.n + 1)*self.GouyPhase - self.k*(X**2 + Y**2)/(2*Rz)))


    def plot_amplitude(self):
        plt.imshow(np.abs(self.HGB), extent=[-self.L, self.L, -self.L, self.L] , cmap= 'gray')
        plt.title(f'Hermite-Gaussian Mode m={self.m}, n = {self.n}, z = {self.z}')
        plt.xlabel('x(m)')
        plt.ylabel('y(m)')
        plt.show()

    def plot_phase(self):
        plt.imshow(np.angle(self.HGB) ,cmap= 'gray')
        plt.title(f'Phase Hermite-Gaussian Mode m={self.m}, n = {self.n}, z = {self.z}')
        plt.xlabel('x(m)')
        plt.ylabel('y(m)')
        plt.show()

    def Hologam(self):
        '''
        Considering a DMD with resolution of 1920x1080
        '''
        Amp = np.abs(self.HGB)
        Amp = Amp/np.max(Amp)

        phi = np.angle(self.HGB)
        pp = np.arcsin(Amp)

        qq = phi

        self.CGH = 0.5 + 0.5 * np.sign(np.cos(pp) + np.cos(qq))



HGM = HermiteGaussian(L = 15e-3,
                      size = 501,
                      n = 3,
                      m = 3,
                      w0 = 4e-3,
                      k = (2*np.pi/632.8e-9),
                      z = 0.375)
HGM.plot_phase()


