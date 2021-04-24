import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataset = pd.read_csv('CSV-of-Stock-Data.csv')
X = dataset.iloc[ : ,   : 1 ].values
Y = dataset.iloc[ : , 1 ].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 1/4, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()



def train():
    
    regressor.fit(X_train, Y_train)
    
def prediction(UserInput):

    train()
    
    Y_pred = regressor.predict(X_test)
    
    test_x = np.array(UserInput).reshape(-1,1)
    
    result = regressor.predict(test_x)
    
    return result[0]