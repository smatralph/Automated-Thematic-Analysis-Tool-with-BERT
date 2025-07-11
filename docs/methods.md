# Methods

1. **Data Extraction**
   - Extracts text from PDFs using PyMuPDF.
   - Extracts text from online pages using BeautifulSoup.
   - Merges all text into a single dataset.

2. **Preprocessing**
   - Converts text to lowercase, removes links and stopwords.
   - Uses SpaCy for lemmatization and sentence segmentation.
   - Keeps only useful parts of speech (nouns, verbs, adjectives).

3. **Theme Clustering**
   - Converts text into vector embeddings using Sentence Transformers.
   - Uses KMeans for clustering.
   - Automatically detects the best number of clusters with Kneed.

4. **Sentiment Analysis**
   - Applies a pre-trained model (`cardiffnlp/twitter-roberta-base-sentiment`).
   - Classifies each theme as positive, neutral, or negative.

5. **Visualization**
   - Displays word clouds, sentiment charts, and cluster composition graphs.
