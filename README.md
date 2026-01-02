Context-Aware AI Decision Automation System
Overview

A client-facing AI decision automation system that analyzes customer requests
using machine learning + business context and recommends the urgency and next action.

The system is built for real-time decision support and runs as an interactive Streamlit application (no API required).

Features

NLP-based request understanding (TF-IDF)

Context-aware ML predictions

Rule-based decision agent for automation

Interactive client UI using Streamlit

Optional database logging for governance & audit

Tech Stack

Python

Streamlit (UI)

Scikit-learn

Pandas, NumPy

SQLite

NLP (TF-IDF Vectorization)

How the System Works

User enters a customer request and context

Text is preprocessed and vectorized

ML model predicts urgency

Decision agent selects the best action

Result is displayed instantly in the UI

Decision is optionally stored in the database

Run Instructions (Streamlit)
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the application
streamlit run streamlit_app.py

3️⃣ Open in browser
http://localhost:8501

Example Input

Customer Request: "My payment failed and no one is responding"

Customer Type: premium

Interaction Count: 3

Severity Score: 8

Example Output

Urgency: HIGH

Action: ESCALATE_TO_HUMAN

Why Streamlit Instead of API?

Faster prototyping and demos

No backend deployment complexity

Real-time interaction

Ideal for client-facing and interview demos

API can be added later if needed

Future Enhancements

Model retraining with feedback loop

Confidence scoring

Dashboard analytics

API wrapper for production deployment

LLM-based decision agent

One-line Summary (perfect for interviews)

An interactive AI system that understands customer issues and automatically decides urgency and actions using machine learning and business rules.

If you want, I can also:

polish this for GitHub

convert it into a research-style abstract

add architecture diagrams

give you interview-ready explanation

Just tell me .