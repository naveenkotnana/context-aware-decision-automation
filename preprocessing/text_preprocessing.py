import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.exceptions import NotFittedError


class TextPreprocessor:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.is_fitted = False

    def clean_text(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"[^a-zA-Z ]", "", text)
        return text

    def fit_transform(self, texts):
        cleaned = [self.clean_text(t) for t in texts]
        self.is_fitted = True
        return self.vectorizer.fit_transform(cleaned)

    def transform(self, texts):
        if not self.is_fitted:
            raise NotFittedError(
                "TextPreprocessor is not fitted. Call fit_transform() first."
            )
        cleaned = [self.clean_text(t) for t in texts]
        return self.vectorizer.transform(cleaned)
