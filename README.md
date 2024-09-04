# customer-segmentation-api
A Flask API for customer segmentation using K-Means clustering, deployed on AWS Elastic Beanstalk. The API accepts customer data (recency, frequency, and monetary) and returns the predicted cluster. Includes configuration files and deployment instructions.


# Flask API Deployment for Customer Segmentation

This repository contains a Flask API that performs customer segmentation using the K-Means clustering algorithm. The API is deployed on AWS Elastic Beanstalk, allowing it to handle requests that classify customers based on recency, frequency, and monetary data.

## Features

- Accepts customer data in JSON format (recency, frequency, and monetary values).
- Returns the predicted cluster based on K-Means clustering.
- Deployed on AWS Elastic Beanstalk for easy scaling and management.
  
## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/flask-api-deployment.git
cd flask-api-deployment



### 2. Install Dependencies

Make sure Python 3.x is installed. Install the required dependencies by running:

bash

pip install -r requirements.txt



### 3. Run the Flask App Locally

To run the Flask app locally, use the following command:

bash

python app.py

The app will be accessible at http://127.0.0.1:5000/.


### 4. Deploy to AWS Elastic Beanstalk

    Install AWS CLI and Elastic Beanstalk CLI:
        Install the AWS CLI.
        Install the Elastic Beanstalk CLI.

    Configure AWS CLI:

    Run the following command and provide AWS credentials:

    bash

aws configure

Initialize the Elastic Beanstalk Environment:

bash

eb init

Create and Deploy the Environment:

bash

    eb create flask-api-env
    eb deploy

Once deployed, Elastic Beanstalk will provide a URL where the API can be accessed.
Usage

To interact with the API, send a POST request with customer data (recency, frequency, monetary):

python

import requests

# Replace with your deployed URL
url = 'http://flask-api-env.us-east-1.elasticbeanstalk.com/predict'

# Sample data
customer_data = {
    'Recency': 10,
    'Frequency': 5,
    'Monetary': 300
}

response = requests.post(url, json=customer_data)
print(f'Predicted Cluster: {response.json()["cluster"]}')

### Files in This Repository

    app.py: The main Flask application.
    requirements.txt: List of dependencies required to run the Flask app.
    Procfile: Instructions for Elastic Beanstalk to run the app.
    kmeans_model.pkl: The trained K-Means model (not included in this repo, must be generated).
    scaler.pkl: The data scaler (not included in this repo, must be generated).
