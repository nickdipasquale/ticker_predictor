# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 07:46:25 2021

@author: immek
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

url = 'https://raw.githubusercontent.com/nickdipasquale/ticker_predictor/main/CSV%20for%20data2.csv'
df = pd.read_csv(url, error_bad_lines=False)
df.dropna(inplace = True) #dropping any blank space

#WordCloud
text = df['Stock'].str.cat(sep=' ') #Showing Stocks for word cloud

#Setting background to color white and removing unwanted words with stopwords
wordcloud = WordCloud(background_color = 'white', 
        stopwords = ['Date','Stock', 'Tickers', 
                     'Open','Close', 'High', 
                     'Low', 'IV', 'under',
                     'over', 'price', 'change', 
                     '%', 'null']).generate(str(text))

plt.figure(figsize=(20,10))
plt.imshow(wordcloud) 
plt.axis("off")
plt.show()


# Ticker mentions
print(df.shape) #using to make sure all rows are being used
x = df['Stock']
y = df.Tickers

plt.rcParams['figure.figsize'] = 25, 10
plt.title ('Ticker Mentions', fontsize=25)
plt.xlabel('Stock', fontsize=18)
plt.ylabel('Tickers', fontsize=16)
plt.scatter(x, y)
plt.show()


#Precent price change
y = df['price change %']
y_indexes = np.arange(len(y))

plt.title ('Percent Change', fontsize=25)
plt.xlabel('Stock', fontsize=18)
plt.ylabel('Percent Change', fontsize=16)
plt.scatter(x,y)
plt.ylim(ymax = 15, ymin = 0)
plt.show()


#Linear Regression Model PC
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = df.iloc[ : , 1 ].values.reshape(-1,1)
Y = df.iloc[ : , 7 ].values.reshape(-1,1)
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 1/4, random_state = 0)
regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)

Y_pred = regressor.predict(X_test)
print("MSE:%.4f" % mean_squared_error(Y_test[:,0], Y_pred[:,0])) 

plt.title ('Linear Regression Model PC', fontsize=25)
plt.xlabel('Tickers', fontsize=18)
plt.ylabel('Price % Change', fontsize=16)
plt.scatter(X_train , Y_train, color = 'red')
plt.plot(X_train , regressor.predict(X_train), color ='blue')
plt.show()


#Linear Regression Model IV
X = df.iloc[ : , 1 ].values.reshape(-1,1)
Y = df.iloc[ : , 6 ].values.reshape(-1,1)
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 1/4, random_state = 0)
regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)

Y_pred = regressor.predict(X_test)
print("MSE:%.4f" % mean_squared_error(Y_test[:,0], Y_pred[:,0]))

plt.title ('Linear Regression Model IV', fontsize=25)
plt.xlabel('Tickers', fontsize=18)
plt.ylabel('IV % Change', fontsize=16)
plt.scatter(X_train , Y_train, color = 'green')
plt.plot(X_train , regressor.predict(X_train), color ='purple')
plt.show()

