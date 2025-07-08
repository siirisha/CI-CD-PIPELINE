from flask import Flask, request, jsonify
import pickle
import os
import pandas as pd

# Define paths
model_path = os.path.join(os.path.dirname(__file__), "..", "models", "failure_predictor.pkl")
vectorizer_path = os.path.join(os.path.dirname(__file__), "..", "models", "vectorizer.pkl")

# Load the trained model and vectorizer
if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
    raise FileNotFoundError("Model or vectorizer file not found. Ensure they are in the 'models/' directory.")

with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

with open(vectorizer_path, "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Initialize Flask app
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    """
    Endpoint to make predictions.
    Expects JSON input with a 'logs' field containing a list of log lines.
    """
    data = request.get_json()
    if not data or "logs" not in data:
        return jsonify({"error": "Invalid input. Provide a 'logs' field with log lines."}), 400

    logs = data["logs"]
    if not isinstance(logs, list):
        return jsonify({"error": "'logs' field must be a list of log lines."}), 400

    # Transform logs using the vectorizer
    transformed_logs = vectorizer.transform(logs)

    # Make predictions
    predictions = model.predict(transformed_logs)

    # Return predictions as JSON
    return jsonify({"predictions": predictions.tolist()})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)