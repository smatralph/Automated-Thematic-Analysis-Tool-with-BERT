from transformers import pipeline
import pandas as pd

def analyze_sentiment(themes):
    """Analyzes sentiment for each theme using a transformer model."""
    classifier = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
    sentiments = []
    for _, row in themes.iterrows():
        result = classifier(row["theme_text"][:512])[0]  # limit text length
        sentiments.append(result)
    sentiment_df = pd.DataFrame(sentiments)
    final = pd.concat([themes, sentiment_df], axis=1)
    return final
