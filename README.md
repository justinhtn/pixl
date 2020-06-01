# Pixl
A simple python package that takes in an image and returns a vector. It uses the Xception model in TensorFlow Keras (pre-trained on Imagenet) to generate image embeddings by returning the value of the 'avg_pool' intermediate NN layer. 

### Dependencies
Tensorflow>=2.0

### Install

`pip install pixl`

### Example notebook

An example colab notebook can be found [here](https://colab.research.google.com/drive/1BaryND4V8VcbTAQlGyrOBIal_PxV2SuU?usp=sharing) which shows how to use the pixl object and generate k-means clusters from the returned image vectors.
