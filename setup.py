from setuptools import setup

setup(name='pixl',
      version='0.1',
      description='Takes an image and returns a dense vector',
      url='https://github.com/justinhtn/pixl',
      author='Justin Houghton',
      author_email='justin.houghton@gmail.com',
      license='MIT',
      packages=['pixl'],
      zip_safe=False,
      install_requires=[
          'tensorflow=>2.2.0',
      ])