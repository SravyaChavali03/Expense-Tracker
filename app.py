from flask import Flask, request, jsonify
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import joblib

# Initialize Flask app
app = Flask(__name__)

# Dummy data for training a simple model
descriptions = ["Pizza Hut", "Shell Gas Station", "Netflix Subscription", "Walmart", "Uber"]
categories = ["Food", "Transport", "Entertainment", "Shopping", "Transport"]

# Train a simple model (or load a pre-trained one)
label_encoder = LabelEncoder()
encoded_descriptions = label_encoder.fit_transform(descriptions)
model = LogisticRegression()
model.fit(encoded_descriptions.reshape(-1, 1), categories)

# Save the model and encoder (for later use)
joblib.dump(model, 'model.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')

# Define the /categorize endpoint
@app.route('/categorize', methods=['POST'])
def categorize_transaction():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        if not data or 'description' not in data:
            return jsonify({"error": "Invalid request: 'description' field is required"}), 400

        # Get the description from the request
        description = data['description']

        # Encode the description and predict the category
        encoded_description = label_encoder.transform([description])
        category = model.predict(encoded_description.reshape(-1, 1))[0]

        # Return the predicted category
        return jsonify({"category": category})

    except Exception as e:
        # Log the error and return a 500 response
        print(f"Error: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True) 