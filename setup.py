from setuptools import setup

setup(name='pixl',
      version='0.1',
      description='A simple package that takes in an image and returns a vector.',
      url='https://github.com/justinhtn/pixl',
      author='Justin Houghton',
      author_email='justin.houghton@gmail.com',
      license='MIT',
      packages=['pixl'],
      zip_safe=False,
      install_requires=[
          'tensorflow>=2.2.0',
      ])