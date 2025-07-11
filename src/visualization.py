import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

def plot_wordcloud(themes):
    text = " ".join(themes["theme_text"])
    wc = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud of Themes")
    plt.show()

def plot_sentiments(sentiment_df):
    plt.figure(figsize=(7, 4))
    sns.countplot(x="label", data=sentiment_df)
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.show()
