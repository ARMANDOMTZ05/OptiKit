import numpy as np
import matplotlib as plt

class Propagator:
    def __init__(self,
                 beam: np.ndarray,
                 L: float,
                 zn: int,
                 z: float,
                 k: float) -> None:
        

        if beam.shape[0] != beam.shape[1]:
            raise ValueError('The shape of the Beam matrix must be NxN')
        
        self.zn = zn
        self.k = k
        self.L = L
        self.N = beam.shape[0]

        self.beam = beam

        x = np.linspace(-L,L,self.N)

        self.x, self.y  = np.meshgrid(x,x)
        self.E_fft = np.fft.fftshift(np.fft.fft2(self.beam))

        self.prop_beam = np.zeros(self.N, self.N, self.zn, dtype=np.complex64)
        self.prop_beam[:,:,0] = self.beam

        self.propagate()


        self.prop_beam

    def Transfer_Function(self, z):
        return np.exp(-1j * z * self.k * np.sqrt(1 - (np.pi*2/self.k)**2 * (self.kx ** 2 + self.ky ** 2)))

    
    def propagate(self):
        x = np.linspace(-self.L,self.L,self.N)
        self.z = np.linspace(0,z,self.zn)
        fx = x * (-1/self.N)
        self.kx, self.ky = np.meshgrid(fx, fx)
        for i,z in enumerate(self.z, 0):
            self.prop_beam[:,:,i] = np.fft.ifft2(self.prop_beam[:,:,i-1] * self.Transfer_Function(z=z))
    
    def plot(self):
        plt.imshow(np.abs(self.prop_beam[:,self.N//2,:]), cmap= 'gray')
        plt.show()