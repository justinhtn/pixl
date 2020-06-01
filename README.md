# Pixl
A simple python package that takes in an image and returns a vector. It uses the Xception model in TensorFlow Keras (pre-trained on Imagenet) to generate image embeddings by returning the value of the 'avg_pool' intermediate NN layer. 

### Dependencies
Tensorflow>=2.0

### Install

pip install git+git://github.com/justinhtn/pixl.git

### Examples

An example notebook can be found https://github.com/justinhtn/pixl/blob/master/example.ipynb which shows how to use the pixl object and generate k-means clusters from the returned image vectors.
