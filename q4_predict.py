
# Machine Learning ZoomCamp - Homework 5
# Author.....: Carlos Manuel de Oliveira Alves
# Created...: 09/10/2022

# Import the library Flask and some packages
from flask import Flask
from flask import request
from flask import jsonify # use this package to connect dictionary to JSON

# Import pickle library to load files
import pickle

# Create function for loading the pickle files
def load(filename):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)

# Load and store the files dictionary vectorizer and the model
dv = load('dv.bin')
model = load('model1.bin')

# Create a flask up
app = Flask('churn')

# Use decorator to add extra functionality to the function predict
@app.route('/predict', methods=['POST'])

# Create a function to predict the probability of getting a credit card
def predict():

    # Use request to the JSON file to python dictionary
    customer = request.get_json()

    # Use the customer data into feature matrix using our dictionary vectorizer transform method
    X = dv.transform([customer])

    # Call model using the method predict proba with X and get the probability
    y_pred = model.predict_proba(X)[0, 1]

    # Define the threshold of the churn
    churn = y_pred >= 0.5

    # Prepare our response to JSON
    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }

    # Returns the prediction of churning
    return jsonify(result)

# Declare the main method of the python file
if __name == "__main":

    # Specify the local host we're running our app
    app.run(debug=True, host='0.0.0.0', port=9696)

