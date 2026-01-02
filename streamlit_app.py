import streamlit as st
import pandas as pd
import numpy as np

from preprocessing.text_preprocessing import TextPreprocessor
from models.ml_model import MLDecisionModel
from decision_agent.decision_agent import DecisionAgent
from database.db import Database


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Context-Aware AI Decision Automation",
    layout="centered"
)

st.title(" Context-Aware AI Decision Automation")
st.caption("Client-side Streamlit application (No API)")


# ---------------- LOAD COMPONENTS SAFELY ----------------
@st.cache_resource
def load_components():
    preprocessor = TextPreprocessor()
    model = MLDecisionModel()
    agent = DecisionAgent()

    db = Database()
    db.initialize()   # safe, one-time

    data = pd.read_csv("./data/raw_requests.csv")

    # Train model once
    X_text = preprocessor.fit_transform(data["request_text"])
    X_num = data[["interaction_count", "severity_score"]].values
    X = np.hstack((X_text.toarray(), X_num))
    y = data["urgency"]

    model.train(X, y)

    return preprocessor, model, agent, db


preprocessor, model, agent, db = load_components()
st.success(" Model loaded and ready")


# ---------------- USER INPUT ----------------
request_text = st.text_area(
    "Customer Request",
    placeholder="e.g. My payment failed and no one is responding"
)

customer_type = st.selectbox(
    "Customer Type",
    ["regular", "premium"]
)

interaction_count = st.slider(
    "Interaction Count",
    1, 10, 1
)

severity_score = st.slider(
    "Severity Score",
    1, 10, 5
)


# ---------------- PROCESS ----------------
if st.button(" Process Request"):
    if request_text.strip() == "":
        st.warning("Please enter a customer request")
    else:
        # Vectorize input
        X_text = preprocessor.transform([request_text])
        X_num = np.array([[interaction_count, severity_score]])
        X = np.hstack((X_text.toarray(), X_num))

        # Predict urgency
        urgency = model.predict(X)[0]

        # Decide action
        action = agent.decide(
            urgency,
            customer_type,
            severity_score
        )

        # Save decision (optional)
        db.insert_decision(request_text, urgency, action)

        # Output
        st.subheader(" Decision Output")
        st.write("Debug message")
        st.write(f"**Urgency:** {urgency}")
        st.write(f"**Action:** {action}")       
        st.success(" Decision processed and saved")
