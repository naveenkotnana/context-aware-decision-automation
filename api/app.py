import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Decision Automation", layout="centered")
st.title(" Context-Aware AI Decision Automation")

# ---- SAFE IMPORTS ----
try:
    from preprocessing.text_preprocessing import TextPreprocessor
    from models.ml_model import MLDecisionModel
    from decision_agent.decision_agent import DecisionAgent
    from database.db import Database
    st.success(" All modules imported")
except Exception as e:
    st.error(f" Import failed: {e}")
    st.stop()

# ---- SAFE LOAD ----
@st.cache_resource
def load_model():
    try:
        pre = TextPreprocessor()
        model = MLDecisionModel()
        agent = DecisionAgent()
    except Exception as e:
        st.error(f" Init error: {e}")
        st.stop()

    try:
        data = pd.read_csv("./data/raw_requests.csv")
    except Exception as e:
        st.error(f" CSV error: {e}")
        st.stop()

    X_text = pre.fit_transform(data["request_text"])
    X_num = data[["interaction_count", "severity_score"]].values
    X = np.hstack((X_text.toarray(), X_num))
    y = data["urgency"]

    model.train(X, y)
    return pre, model, agent

preprocessor, ml_model, decision_agent = load_model()
st.success(" Model loaded")

# ---- UI ----
text = st.text_area("Customer request")
severity = st.slider("Severity", 1, 10, 5)
ctype = st.selectbox("Customer type", ["regular", "premium"])

if st.button("Process"):
    X_text = preprocessor.transform([text])
    X = np.hstack((X_text.toarray(), [[1, severity]]))
    urgency = ml_model.predict(X)[0]
    action = decision_agent.decide(urgency, ctype, severity)

    st.write("Urgency:", urgency)
    st.write("Action:", action)
