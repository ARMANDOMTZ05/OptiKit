import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre, factorial


def LP(n, alpha, x):

    L_n_alpha = genlaguerre(n, alpha)(x)

    return L_n_alpha

class LaguerreGaussian:
    def __init__(self,
                 L: float,
                 size: int,
                 p: int,
                 l: int,
                 w0: float,
                 k: float,
                 z: float) -> None:
        
        if p < 0:
            raise ValueError('p must be positive')
        
        self.size = size
        self.L = L
        self.w0 = w0
        self.p = p
        self.l = l
        self.k = k
        self.z = z


        x, y = np.linspace(-self.L, self.L, self.size), np.linspace(-self.L, self.L, self.size)
        Y, X = np.meshgrid(x, y)

        r = np.sqrt(X ** 2 + Y ** 2)
        theta = np.arctan2(Y,X)

        if self.z == 0:
            lgb = (1/self.w0) * (r*np.sqrt(2)/self.w0)**(np.abs(self.l)) * np.exp(-r**2/self.w0**2) * LP(self.p, np.abs(self.l), 2*r**2/self.w0**2) * np.exp(-1j*self.l*theta)

        else:
            zr = 1/2 * self.k * self.w0 ** 2
            wz = self.w0 * np.sqrt(1 + (z/zr) ** 2)
            Rz = z * (1 + (zr / z) ** 2)
            CMnumber = np.abs(self.l) + 2 * self.p

            self.GouyPhase = (CMnumber + 1) * np.arctan(z/zr)

            lgb = (1/wz) * (r*np.sqrt(2)/wz)**(np.abs(self.l)) * np.exp(-r**2/wz**2) * LP(self.p, np.abs(self.l), 2*r**2/wz**2) * np.exp(-1j*self.k*r**2/(2*Rz)) * np.exp(-1j*self.l*theta) * np.exp(1j * self.GouyPhase)

        Norm = np.sqrt((2*factorial(self.p))/(np.pi*factorial(self.p + np.abs(self.l))))

        self.LGB = lgb * Norm

    def plot_amplitude(self):
        plt.imshow(np.abs(self.LGB), extent=[-self.L, self.L, -self.L, self.L] , cmap= 'gray')
        plt.title(f'Laguerre-Gaussian Mode l = {self.l}, p = {self.p}, z = {self.z}')
        plt.xlabel('x(m)')
        plt.ylabel('y(m)')
        plt.show()

    def plot_phase(self):
        plt.imshow(np.angle(self.LGB) ,cmap= 'gray')
        plt.title(f'Phase Laguerre-Gaussian Mode l = {self.l}, p = {self.p}, z = {self.z}')
        plt.xlabel('x(m)')
        plt.ylabel('y(m)')
        plt.show()





LGB = LaguerreGaussian(L = 15e-3,
                      size = 501,
                      p = 3,
                      l = 3,
                      w0 = 4e-3,
                      k = (2*np.pi/632.8e-9),
                      z = 0.375)
LGB.plot_phase()



