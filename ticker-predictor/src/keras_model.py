import numpy as np
import tensorflow as tf
import keras

from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# load the dataset
dataset = loadtxt('CSV-prototype-keras-output2.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:5]
Y = dataset[:,5:7]

in_dim = X.shape[1]
out_dim = Y.shape[1]

xtrain, xtest, ytrain, ytest=train_test_split(X, Y, test_size=20)

model = Sequential()
model.add(Dense(5, input_dim=in_dim, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(out_dim))
model.compile(loss="mse", optimizer="adam")

 

model.summary()

def train():
    model.fit(xtrain, ytrain, epochs=100, batch_size=10, verbose=0)
    
def predict(UserInput):
    train()
    
    x_reshape = np.array(UserInput).reshape(1,5)
    result = model.predict(x_reshape)
    return result[0]