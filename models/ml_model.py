import joblib
import os
from sklearn.linear_model import LogisticRegression


class MLDecisionModel:
    def __init__(self, model_path="models/model.pkl"):
        self.model_path = model_path
        self.model = LogisticRegression(max_iter=1000)
        self.is_trained = False

    def train(self, X, y):
        self.model.fit(X, y)
        self.is_trained = True

    def predict(self, X):
        if not self.is_trained:
            # Streamlit-safe
            return ["UNKNOWN"] * len(X)
        return self.model.predict(X)

    def save(self):
        # Ensure directory exists (critical)
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        joblib.dump(self.model, self.model_path)

    def load(self):
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
            self.is_trained = True
