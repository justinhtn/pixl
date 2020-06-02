# Pixl
A simple python package that takes in an image and returns an embedding. It uses the [Xception model](https://www.tensorflow.org/api_docs/python/tf/keras/applications/xception) in TensorFlow Keras (pre-trained on Imagenet) to generate image embeddings by returning the value of the 'avg_pool' intermediate NN layer. 

### Dependencies
Tensorflow>=2.0

### Install

`pip install pixl`

### Example notebook

A colab notebook can be found [here](https://github.com/justinhtn/pixl/blob/master/colab_example.ipynb) which provides an example of using the `util` module's `get_vec` method to generate image embeddings which when used to fit a kmeans clustering algorithm, can do a pretty good job at predicting classes.

### Usage

```python
from pixl.utils import Pixl

# instantiate a pixl object
p_obj = Pixl()
# set path for img files
img_path = './Images/dog_1.jpg'
# get image embedding
vec = p_object.get_vec(img_path)
```
