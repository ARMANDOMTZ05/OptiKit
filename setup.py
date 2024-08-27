from setuptools import setup

setup(
   name='pyOptics',
   version='0.1.1a',
   description='A basic optics module',
   long_description=open('README.md').read().strip(),
   author='Armando Martinez',
   author_email='ar.martinez.hdz@hotmail.com',
   url= 'https://github.com/ARMANDOMTZ05/pyOptics',
   py_modules=['Gaussian', 'Beam', 'HermiteGauss', 'InceGauss', 'LaguerreGauss', 'optics'],
   packages=['pyoptics'],
   install_requires=['matplotlib', 'numpy', 'scipy', 'PIL'],
   keywords= 'numpy, optics, holography, slm, python3, wavefront shaping',
   classifiers= ['Development Status :: 4 - Beta',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3.10'],
   python_requires='>=3.10',
)