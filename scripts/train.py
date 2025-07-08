import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Define paths
features_path = "data/features.csv"
labels_path = "data/labels.csv"
model_path = "models/failure_predictor.pkl"

# Ensure directories exist
os.makedirs("models", exist_ok=True)

# Load preprocessed features and labels
def load_data(features_file, labels_file):
    features = pd.read_csv(features_file)
    labels = pd.read_csv(labels_file)
    return features, labels

# Train a Logistic Regression model
def train_model(features, labels):
    model = LogisticRegression()
    model.fit(features, labels.values.ravel())  # Flatten labels to 1D array
    return model

# Save the trained model
def save_model(model, model_file):
    with open(model_file, "wb") as file:
        pickle.dump(model, file)

def main():
    # Load data
    features, labels = load_data(features_path, labels_path)
    
    # Train model
    model = train_model(features, labels)
    
    # Save model
    save_model(model, model_path)
    print(f"Model training complete. Model saved to '{model_path}'.")

if __name__ == "__main__":
    main()