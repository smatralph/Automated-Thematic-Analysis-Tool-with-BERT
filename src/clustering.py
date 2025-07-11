from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer
from kneed import KneeLocator
import pandas as pd

def generate_embeddings(sentences):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model.encode(sentences)

def find_optimal_clusters(embeddings, max_clusters=10):
    distortions = []
    for k in range(2, max_clusters + 1):
        model = KMeans(n_clusters=k, random_state=42)
        model.fit(embeddings)
        distortions.append(model.inertia_)
    kneedle = KneeLocator(range(2, max_clusters + 1), distortions, curve="convex", direction="decreasing")
    return kneedle.elbow or 5

def generate_themes(text, num_clusters=None):
    sentences = text.split(". ")
    embeddings = generate_embeddings(sentences)
    if not num_clusters:
        num_clusters = find_optimal_clusters(embeddings)
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(embeddings)
    df = pd.DataFrame({"sentence": sentences, "cluster": kmeans.labels_})
    themes = df.groupby("cluster")["sentence"].apply(lambda x: " ".join(x)).reset_index()
    themes.rename(columns={"sentence": "theme_text"}, inplace=True)
    return themes
