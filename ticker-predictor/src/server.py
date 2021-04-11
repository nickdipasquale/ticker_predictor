# import Flask
import random
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
    print(ticker)

    # convert dictionary to JSON string
    result = str(random.randint(-5, 5))

    return result
    

# Run the server
if __name__ == '__main__':
    
    # start the server
    app.run(port = 5000)