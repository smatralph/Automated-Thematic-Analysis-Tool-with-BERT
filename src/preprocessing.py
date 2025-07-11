import re
import nltk
import spacy

nltk.download("stopwords", quiet=True)
from nltk.corpus import stopwords

nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words("english"))

def clean_text(text):
    """Removes unwanted characters and extra spaces."""
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"http\S+|www\S+", "", text)
    return text.strip()

def preprocess_text(text):
    """Tokenizes, removes stopwords, and lemmatizes."""
    text = clean_text(text)
    doc = nlp(text.lower())
    tokens = [
        token.lemma_
        for token in doc
        if token.is_alpha and token.text not in stop_words
    ]
    return " ".join(tokens)
