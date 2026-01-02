Context-Aware AI Decision Automation System
 Overview

This project is an end-to-end AI-powered decision automation system that analyzes customer requests and automatically determines:

How urgent the request is

What action should be taken next

It combines Natural Language Processing (NLP), Machine Learning, and business rule-based decision logic to mimic how real enterprise systems handle customer support and operational workflows.

The application runs as an interactive Streamlit app (no API required) and is designed for real-time decision support.

 Problem Statement

In real-world organizations (fintech, telecom, e-commerce, support centers):

Thousands of customer requests arrive daily

Manual triaging is slow and inconsistent

Pure rule-based systems lack flexibility

Pure ML systems lack explainability

 Solution

This system combines:

ML → to understand text and predict urgency

Rules → to enforce business logic and control decisions

Result: Fast, scalable, and explainable decision automation.

 System Architecture
User Input (Streamlit UI)
        ↓
Text Preprocessing (TF-IDF, Cleaning)
        ↓
ML Model (Logistic Regression)
        ↓
Urgency Prediction
        ↓
Decision Agent (Business Rules)
        ↓
Final Action
        ↓
(Optional) SQLite Database Logging

🔍 Key Features

NLP-based customer request understanding

Context-aware ML predictions

Rule-based decision agent for explainability

Interactive UI using Streamlit

Optional database logging for audit & governance

Modular, scalable project structure

 Tech Stack

Python

Streamlit (UI)

Scikit-learn

Pandas, NumPy

SQLite

NLP (TF-IDF Vectorization)

Git & GitHub

 Project Structure
context-aware-decision-automation/
│
├── streamlit_app.py          # Main Streamlit application
├── data/
│   └── raw_requests.csv      # Training dataset
│
├── preprocessing/
│   └── text_preprocessing.py # Text cleaning & TF-IDF
│
├── models/
│   └── ml_model.py           # ML model (Logistic Regression)
│
├── decision_agent/
│   └── decision_agent.py     # Business decision rules
│
├── database/
│   └── db.py                 # SQLite database logic
│
├── requirements.txt
└── README.md

 File-by-File Explanation
streamlit_app.py

Entry point of the application

Builds the UI

Collects user inputs

Runs ML prediction and decision logic

Displays urgency and action

preprocessing/text_preprocessing.py

Cleans raw text (lowercase, remove symbols)

Converts text into numerical features using TF-IDF

Ensures safe usage during Streamlit reruns

models/ml_model.py

Implements Logistic Regression model

Trains on historical request data

Predicts urgency (HIGH, LOW, UNKNOWN)

Designed to be Streamlit-safe

decision_agent/decision_agent.py

Converts ML output into business actions

Applies rules like:

High urgency + premium → escalate

Low severity → auto-resolve

Ensures explainability and control

database/db.py

Stores request, urgency, and action

Used for audit, monitoring, and future retraining

Optional for demo (system works without DB)

data/raw_requests.csv

Training dataset

Contains:

request text

interaction count

severity score

urgency label

 How to Clone & Run the Project
1️⃣ Clone the repository
git clone https://github.com/naveenkotnana/context-aware-decision-automation.git
cd context-aware-decision-automation

2️⃣ Create and activate virtual environment (recommended)

Use Python 3.10 or 3.11

python3 -m venv venv
source venv/bin/activate   # Linux / macOS


(Windows)

venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the Streamlit application
streamlit run streamlit_app.py

5️⃣ Open in browser
http://localhost:8501

 Example Input

Customer Request

My payment failed and no one is responding


Customer Type: premium

Interaction Count: 3

Severity Score: 8

 Example Output
Urgency: HIGH
Action: ESCALATE_TO_HUMAN

 Why Streamlit Instead of API?

Faster prototyping

No backend deployment complexity

Real-time interaction

Ideal for demos and interviews

Can be extended to FastAPI later

 Future Enhancements

Feedback loop for model retraining

Confidence scores for predictions

Analytics dashboard

REST API wrapper

LLM-based decision agent

 One-Line Summary (Interview Ready)

An AI system that understands customer issues and automatically determines urgency and actions using NLP, machine learning, and business rules.