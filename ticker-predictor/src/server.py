# import Flask
import random
import yfinance as yf
import json
from flask import Flask, send_from_directory, request, json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


# Send the result from machine learning
# Endpoint is "result"
@app.route('/result', methods=["GET"])
def result():
    # Get ticker name from url parameter
    ticker = request.args.get("ticker")
    mentions = request.args.get("mentions")
    print(ticker)
    print(mentions)

    # Get the last closing price from yahoo finance
    todays_close = yf.Ticker(ticker).history(period='1d')['Close'][0]
    print(todays_close)

    # convert dictionary to JSON string
    result = str(random.randint(-5, 5))

    return result
    

# Run the server
if __name__ == '__main__':
    
    # start the server
    app.run(port = 5000)