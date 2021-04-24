# import Flask
import random
import yfinance as yf
import json
import implied_volatility as iv
import linear_regression as lr
import keras_model as km
from flask import Flask, send_from_directory, request, json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/linearreg', methods=["GET"])
def linearreg():
    # Get ticker name from url parameter
    ticker = request.args.get("ticker")
    mentions = request.args.get("mentions")
    print(ticker)
    print(mentions)

    stockInfo = yf.Ticker(ticker).info

    # Get the current price from yahoo finance
    price = stockInfo["regularMarketPrice"]
    print(price)

    prediction = lr.prediction(mentions) / 200
    print(prediction)

    impliedv = iv.prediction(mentions)
    print(impliedv)

    result = {
        "prediction": str(round(prediction * 100, 3)),
        "price": str(price),
        "prediction_high": str(round((prediction * price) + price, 2)),
        "prediction_low": str(round((1 - prediction) * price, 2)),
        "stock_info": stockInfo["longBusinessSummary"],
        "impliedv": str(round(impliedv, 2))
    }

    resultString = json.dumps(result)

    print(resultString)

    return result


@app.route('/keras', methods=["GET"])
def keras():
    # Get ticker name from url parameter
    ticker = request.args.get("ticker")
    mentions = request.args.get("mentions")
    print(ticker)
    print(mentions)

    stockInfo = yf.Ticker(ticker).info

    # Get the current price from yahoo finance
    price = stockInfo["regularMarketPrice"]
    openp = stockInfo["open"]
    close = stockInfo["previousClose"]
    low = stockInfo["dayLow"]
    high = stockInfo["dayHigh"]

    prediction = km.predict([float(mentions), float(
        openp), float(close), float(high), float(low)])
    print(prediction)

    result = {
        "prediction": str(round(prediction[1], 3)),
        "price": str(price),
        "prediction_high": str(round(((prediction[1] / 100) * price) + price, 2)),
        "prediction_low": str(round((1 - (prediction[1] / 100)) * price, 2)),
        "stock_info": stockInfo["longBusinessSummary"],
        "impliedv": str(round(prediction[0], 3))
    }

    resultString = json.dumps(result)

    print(resultString)

    return result


# Run the server
if __name__ == '__main__':

    # start the server
    app.run(port=5000)
