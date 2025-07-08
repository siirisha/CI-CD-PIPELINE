# scripts/preprocess.py

import os
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import pickle

# Define paths
raw_logs_path = "data/raw_logs.txt"  # Replace with the actual path to your raw Jenkins logs
features_path = "data/features.csv"
labels_path = "data/labels.csv"
vectorizer_path = "models/vectorizer.pkl"

# Ensure directories exist
os.makedirs("data", exist_ok=True)
os.makedirs("models", exist_ok=True)

# Load raw Jenkins logs
def load_logs(file_path):
    with open(file_path, "r") as file:
        logs = file.readlines()
    return logs

# Clean log data
def clean_logs(logs):
    cleaned_logs = [re.sub(r"\s+", " ", log.strip()) for log in logs]
    return cleaned_logs

# Label each line based on presence of errors
def label_logs(logs):
    error_keywords = ["error", "failed", "exception", "critical"]
    labels = [1 if any(keyword in log.lower() for keyword in error_keywords) else 0 for log in logs]
    return labels

# Transform logs into numerical features
def transform_logs(logs):
    vectorizer = CountVectorizer()
    features = vectorizer.fit_transform(logs)
    return features, vectorizer

# Save features, labels, and vectorizer
def save_data(features, labels, vectorizer):
    # Save features and labels
    pd.DataFrame(features.toarray()).to_csv(features_path, index=False)
    pd.DataFrame(labels, columns=["label"]).to_csv(labels_path, index=False)
    
    # Save vectorizer
    with open(vectorizer_path, "wb") as file:
        pickle.dump(vectorizer, file)

def main():
    # Load raw logs
    logs = load_logs(raw_logs_path)
    
    # Clean logs
    cleaned_logs = clean_logs(logs)
    
    # Label logs
    labels = label_logs(cleaned_logs)
    
    # Transform logs into numerical features
    features, vectorizer = transform_logs(cleaned_logs)
    
    # Save features, labels, and vectorizer
    save_data(features, labels, vectorizer)
    print("Preprocessing complete. Features and labels saved to 'data/' and vectorizer saved to 'models/vectorizer.pkl'.")

if __name__ == "__main__":
    main()