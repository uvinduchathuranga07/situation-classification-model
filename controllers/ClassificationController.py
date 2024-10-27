import numpy as np
from flask import request, jsonify

from app import app
from services.serviceImpl.service import  predict_coral


@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    input_data = request.json
    # new_data = np.array([[input_data]])
    # Make prediction
    predicted_class = predict_coral(input_data)
    # Return the result
    return jsonify({'data': {"Predicted Situation:":predicted_class}})
@app.route('/predict', methods=['GET'])
def predicts():
    return jsonify({'data':"OK"})
