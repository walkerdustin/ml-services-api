import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
import pickle
import numpy as np
import sklearn

# model = tf.keras.models.load_model('objectDumps/wine_NN_model_12epochs')



class MLmodel:
    def __init__(self) -> None:
       self.model = tf.keras.models.load_model('objectDumps/wine_NN_model_12epochs')
       self.scaler = pickle.load(open('objectDumps/scaler.sav', 'rb'))
       
    def predict(self, x: list):
        print(f'{x = }')
        x = np.array( [x] ) 
        print(x)
        print(f'{x = }')
        X = self.scaler.transform(x) 
        prediction = self.model.predict( X )[0] *10
        return prediction

       
