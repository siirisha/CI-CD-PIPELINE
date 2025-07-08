# 🔍 CI/CD Failure Predictor using AI

This project is a simple AI-powered system that predicts potential build failures in Jenkins pipelines by analyzing logs. Built using Python, Flask, and Logistic Regression.

---

## 📁 Project Structure

ci-failure-predictor/
├── data/                 # Raw logs, processed features, and labels
│   ├── raw_logs.txt
│   ├── features.csv
│   └── labels.csv
├── models/               # Trained model and vectorizer
│   ├── failure_predictor.pkl
│   └── vectorizer.pkl
├── scripts/              # Preprocessing and training scripts
│   ├── preprocess.py
│   └── train.py
├── app/                  # Flask API to serve predictions
│   └── app.py
├── notebooks/            # Jupyter notebooks for experiments (optional)
│   └── model_dev.ipynb
├── Jenkinsfile           # To integrate into a Jenkins pipeline
├── requirements.txt
└── README.md


---

## ✅ Setup and Execution

### Step 1: Preprocess Logs
This script:
- Reads logs from `data/raw_logs.txt`
- Cleans and labels lines
- Converts to feature vectors
- Saves outputs to `data/` and `models/`


python scripts/preprocess.py


---

### Step 2: Train the Model
Trains a Logistic Regression model using features and labels.


python scripts/train.py


---

### Step 3: Run Flask API
Serves the model for real-time predictions.


cd app
python app.py


API will be available at: `http://127.0.0.1:5000/predict`

---

### Step 4: Test the API
Use curl or Postman to send logs and receive predictions.


curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"logs": ["Build started", "Tests passed", "ERROR: Failed to deploy"]}'


Response:
json
{"predictions": [0, 0, 1]}


---

## 🔮 Future Enhancements
- Integrate with Jenkins pipeline (Jenkinsfile included)
- Use Slack/Webhook for alerts
- Enhance model with historical logs or advanced NLP (e.g., BERT)

---

## 📦 Requirements
Install dependencies:

pip install -r requirements.txt



