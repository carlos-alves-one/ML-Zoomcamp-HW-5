
# Machine Learning ZoomCamp - Homework 5
# Author.....: Carlos Manuel de Oliveira Alves
# Created...: 09/10/2022

# Import pickle library to load files
import pickle

# Create function for loading the pickle files
def load(filename):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)

# Load and store the files dictionary vectorizer and the model
dv = load('dv.bin')
model = load('model1.bin')

# Declare dictionary to score a customer
customer = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"} 

# Use our dictionary vectorizer to transform the customer score and store with X
X = dv.transform([customer])

# Use our model with the function proba and store with y_pred
y_pred = model.predict_proba(X)[0, 1]

# Print the prediction of our model
print(y_pred)

# Answer for quastion 3 : 0.16213414434326598