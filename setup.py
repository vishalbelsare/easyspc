from setuptools import setup


setup(name='spc-svd',
      description='Sparse Principal Components computation based on data matrix SVD',
      version='0.0.1',
      url='https://github.com/aboyker/SPCA',
      author='Alexandre Boyker',
      author_email='alainalain328@gmail.com',
      license='Apache2',
      
      packages=['spc-svd'],
      install_requires=[
          'PyWavelets'
      ]
)