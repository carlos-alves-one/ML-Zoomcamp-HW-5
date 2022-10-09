
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

# Use decorator to add extra functionality to the function predict
@app.route('/predict', methods=['POST'])

# Create a function to predict the probability of getting a credit card
def predict():

    # Use request to the JSON file to python dictionary
    customer = request.get_json()

    