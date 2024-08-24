from setuptools import setup

setup(
   name='pyOptics',
   version='1.0',
   description='Aa basic optics module',
   author='Armando Martinez',
   author_email='ar.martinez.hdz@hotmail.com',
   packages=['pyoptics'],
   install_requires=['matplotlib', 'numpy', 'scipy', 'PIL'], #external packages as dependencies
)