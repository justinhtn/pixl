# Pixl
A simple python package that takes in an image and returns an embedding. It uses the [Xception model](https://www.tensorflow.org/api_docs/python/tf/keras/applications/xception) in TensorFlow Keras (pre-trained on Imagenet) to generate image embeddings by returning the value of the 'avg_pool' intermediate NN layer. 

### Dependencies
Tensorflow>=2.0

### Install

`pip install pixl`

### View in deepnote

<a href="https://deepnote.com/@justin-houghton-190b/pixl-XmsZNhTxRZeBcjwLTpiBtQ?utm_campaign=pixl&utm_medium=publishing&utm_source=copy_link"> <img src="https://beta.deepnote.com/buttons/launch-in-deepnote.svg"> </a>

This notebook provides an example of using the module's `get_vec` method to generate feature vectors to fit a kmeans clustering algorithm. Becuase it's using a pretrained keras model, it can do a pretty good job at clustering simple classes.

### Usage

```python
from pixl.utils import Pixl

# setting directory of sample images and grabbing file_names
img_dir = './Images'

filenames = []
for file in os.listdir(img_dir):
    filenames.append(os.fsdecode(file))
    
# instantiate a pixl object
p_obj = Pixl()

#### Use the pixl object's get_vec method to get your vector ####
def get_vec(img_dir, filenames):
  """
  Returns a list of vectors and a list of labels.

  Args:
  filenames (str): string specifying the name of each file.
  
  Returns:
  vectors (lst): list of vectors representing image files.
  labels (lst): list of labels taken from file names.
  """
  vectors = []
  labels = []

  for file in filenames:
      vec = p_object.get_vec(img_dir + '/' + file)
      vectors.append(vec)
      label = file.split('.')[0]
      labels.append(label)

  return labels, vectors
    
```
