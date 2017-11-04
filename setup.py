from setuptools import setup


setup(name='easyspc',
      description='Sparse Principal Components computation based on data matrix SVD',
      version='0.0.3',
      url='https://github.com/aboyker/easyspc',
      author='Alexandre Boyker',
      author_email='alainalain328@gmail.com',
      license='Apache2',
      
      packages=['easyspc'],
      install_requires=[
          'PyWavelets',
            'numpy'
      ]
)
