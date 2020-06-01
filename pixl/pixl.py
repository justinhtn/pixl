from tensorflow import keras
from tensorflow.keras.applications import xception
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.backend import expand_dims

model_target_size = (299,299)

class Pixl(object):
    
    def __init__(self):
        
        model = xception.Xception(weights='imagenet', pooling='avg')
        layer_name = 'avg_pool'
        self.intermediate_layer_model = keras.Model(inputs=model.input,
                                               outputs=model.get_layer(layer_name).output)

    def get_vec(self, img_path):
        """
        Return image vector using output of intermediate NN model layer.

        Args:
        img_path (str): string specifying location of image.
        
        Returns:
        layer_output (numpy array): numpy array of intermediate layer.
        """

        # loads image and returns a pil object
        img = image.load_img(img_path, target_size= model_target_size)
        # uses pil object and returns a 3d numpy array
        x = image.img_to_array(img)
        # adds additional dimension. Model expects 4 and we currently have 3. 
        x = expand_dims(x, axis=0)
        # pre processing numpy array scaled between -1 and 1
        x = xception.preprocess_input(x)
        # get output of intermediate layer
        intermediate_layer_output = self.intermediate_layer_model.predict(x)

        return intermediate_layer_output[0]