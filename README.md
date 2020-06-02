# Pixl
A simple python package that takes in an image and returns an embedding. It uses the [Xception model](https://www.tensorflow.org/api_docs/python/tf/keras/applications/xception) in TensorFlow Keras (pre-trained on Imagenet) to generate image embeddings by returning the value of the 'avg_pool' intermediate NN layer. 

### Dependencies
Tensorflow>=2.0

### Install

`pip install pixl`

### Example notebook

A colab notebook can be found [here](https://github.com/justinhtn/pixl/blob/master/colab_example.ipynb) which provides an example of using the `util` module's `get_vec` method to generate image embeddings which when used to fit a kmeans clustering algorithm, can do a pretty good job at predicting classes.