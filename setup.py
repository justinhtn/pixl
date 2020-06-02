from distutils.core import setup
from setuptools import find_packages

setup(name='pixl',
      version='0.1.6.2',
      description='A simple package that takes in\
      an image and returns a vector.',
      url='https://github.com/justinhtn/pixl',
      author='Justin Houghton',
      author_email='justin.houghton@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      python_requires='>=3.6')