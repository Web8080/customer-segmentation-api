from flask import Flask, request, jsonify
import pickle
import pandas as pd

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model and scaler from disk
with open('kmeans_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request (expecting JSON format)
    data = request.get_json()
    
    # Convert the data into a pandas DataFrame
    new_customer = pd.DataFrame(data, index=[0])
    
    # Apply the same scaling transformation used during training
    new_customer_scaled = scaler.transform(new_customer[['Recency', 'Frequency', 'Monetary']])
    
    # Use the K-Means model to predict the customer's cluster
    cluster_label = model.predict(new_customer_scaled)
    
    # Return the result as JSON
    return jsonify({'cluster': int(cluster_label[0])})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
