
# Machine Learning ZoomCamp - Homework 5
# Author.....: Carlos Manuel de Oliveira Alves
# Created...: 09/10/2022

# Import the library requests
import requests

# Declare our URL for our localhost
url = "http://localhost:9696/predict"

# Declare dictionary to score a customer
customer = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}

# Store the response from our model
response = requests.post(url, json=customer).json()

# Print our response from our model
print(response)
