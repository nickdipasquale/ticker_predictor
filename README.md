# ticker_predictor
CMPSC445 Final Project

## Data Visualization ##
ProjectGraphs.py file is code for visualizing the data.

PrjectVisualTesting.ipynb is where visualization was tested for deciding which graphs to use and bug testing.  Not all code works in this file.

## Machine Learning Testing ##
MachineLearningTests.ipynb is some of the code we tried and tested.  Code is broken and will not work but is to show some options we were trying.

## How to Run ##
The Ticker Predictor web application is built using Angular and our machine learning algorithms are deployed on a separate Python web server. To set up and run our code, you must first clone our repository using this link: https://github.com/nickdipasquale/ticker_predictor.git. 

Some prerequisites are required to run our system. You must have Python and Angular installed on the host machine. To run the Python web server, open a Windows PowerShell application and browse to the ticker-predictor/src folder. Run the command “python .\server.py”. If any required packages are missing, install them using pip. To run the Angular web application, open another WIndows PowerShell application and browse to the ticker-predictor folder. Run the command "ng serve -o". Once the app is built and running a browser tab will automatically open with the application running.
