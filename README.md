Context-Aware AI Decision Automation System
Overview

This project is an end-to-end AI-driven decision support system designed to automatically analyze customer requests and recommend the urgency level and next best action.

The system combines Natural Language Processing (NLP), Machine Learning, and rule-based decision logic to simulate how real-world enterprise support and operations teams triage and handle incoming requests.

The application is implemented as a Streamlit-based interactive interface, making it suitable for demos, client-facing explanations, and interviews without requiring backend API deployment.

Problem Statement

In large-scale customer support and operations environments:

Thousands of requests are received daily

Manual triaging is time-consuming and inconsistent

High-priority issues may be delayed

Pure rule-based systems lack flexibility

Pure ML systems lack explainability

There is a need for a system that is both intelligent and controllable.

Solution Approach

This project addresses the problem by combining:

NLP and Machine Learning to understand and classify customer requests

Contextual signals such as customer type, severity, and interaction history

Rule-based decision logic to ensure explainable and business-aligned outcomes

The result is a context-aware, scalable, and interpretable decision automation system.

System Architecture
User Input (Streamlit UI)
        ↓
Text Preprocessing (Cleaning + TF-IDF)
        ↓
Machine Learning Model (Logistic Regression)
        ↓
Urgency Prediction
        ↓
Decision Agent (Business Rules)
        ↓
Recommended Action
        ↓
(Optional) Database Logging

Key Features

NLP-based customer request understanding

Context-aware urgency prediction using machine learning

Rule-based decision agent for explainability and control

Interactive Streamlit user interface

Optional SQLite-based logging for audit and analysis

Modular and extensible project structure

Technology Stack

Python

Streamlit

Scikit-learn

Pandas, NumPy

SQLite

NLP using TF-IDF vectorization

Git and GitHub

Project Structure
context-aware-decision-automation/
│
├── streamlit_app.py          # Main application entry point
├── data/
│   └── raw_requests.csv      # Training dataset
│
├── preprocessing/
│   ├── __init__.py
│   └── text_preprocessing.py # Text cleaning and vectorization
│
├── models/
│   ├── __init__.py
│   └── ml_model.py           # Machine learning model logic
│
├── decision_agent/
│   ├── __init__.py
│   └── decision_agent.py     # Business decision rules
│
├── database/
│   ├── __init__.py
│   └── db.py                 # Database operations
│
├── requirements.txt
└── README.md

Input and Output
Inputs

Customer request text

Customer type (regular or premium)

Interaction count

Severity score (1–10)

Outputs

Urgency level (HIGH, LOW, UNKNOWN)

Recommended action, such as:

ESCALATE_TO_HUMAN

AUTO_RESOLVE

ROUTE_TO_OPERATIONS

MANUAL_REVIEW

Example Scenario

Input

Request: “My payment failed and no one is responding”

Customer Type: Premium

Interaction Count: 3

Severity Score: 8

Output

Urgency: HIGH
Action: ESCALATE_TO_HUMAN

Getting Started
1. Clone the Repository
git clone https://github.com/naveenkotnana/context-aware-decision-automation.git
cd context-aware-decision-automation

2. Create and Activate a Virtual Environment

Python 3.10 or 3.11 is recommended.

python3 -m venv venv
source venv/bin/activate   # Linux / macOS


Windows:

venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the Application
streamlit run streamlit_app.py

5. Access the Application

Open the following URL in your browser:

http://localhost:8501

Why Streamlit

Streamlit was chosen to:

Enable rapid prototyping and demonstrations

Avoid backend deployment complexity

Provide real-time interaction for users

Support easy transition to an API-based architecture if required

Future Enhancements

Feedback loop for model retraining

Confidence scores for predictions

Analytics and monitoring dashboard

REST API wrapper for production deployment

Integration with large language models for advanced reasoning

Summary

This project demonstrates how NLP, machine learning, and business rules can be combined to build a practical, explainable, and scalable decision automation system suitable for real-world enterprise use cases.
