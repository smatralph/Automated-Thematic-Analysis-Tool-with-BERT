# NLP Integrated Thematic Analysis Tool

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A natural language processing (NLP) based tool that automates thematic analysis in qualitative research by extracting data, clustering themes, and performing sentiment analysis using transformer-based models.

## Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Installation](#installation)
* [Quick Start](#quick-start)
* [Data Requirements](#data-requirements)
* [Methodology](#methodology)
* [Project Structure](#project-structure)
* [Usage Examples](#usage-examples)
* [Visualization Outputs](#visualization-outputs)
* [Evaluation and Validation](#evaluation-and-validation)
* [Contributing](#contributing)
* [Citation](#citation)
* [License](#license)
* [Acknowledgments](#acknowledgments)

---

## Overview

This project introduces a practical tool for automating thematic analysis using NLP techniques. It supports researchers in identifying and visualizing key themes, patterns, and sentiments from academic papers, transcripts, or reports. The tool integrates text extraction, preprocessing, clustering, and transformer-based sentiment analysis in a single pipeline.

**Key Applications:**

* Academic literature review automation
* Qualitative research support
* Thematic synthesis for large text datasets
* Policy and social research insights
* Sentiment tracking in interviews or surveys

---

## Features

* Automated Text Extraction using BeautifulSoup and PyMuPDF
* Data Cleaning Pipeline with tokenization, stopword removal, and lemmatization
* Transformer Integration using Hugging Face models for sentiment and topic scoring
* Theme Generation through clustering and semantic similarity analysis
* Sentiment Analysis for polarity classification (positive, neutral, negative)
* Visualizations including word clouds, bar charts, and cluster maps
* Export Results as CSV or JSON files

---

## Installation

### Prerequisites

* Python 3.8 or later
* pip package manager
* Internet connection for transformer model downloads

### Setup

1. Clone the repository

   ```bash
   git clone https://github.com/smatralph/Thematic-Analysis-Tool.git
   cd Thematic-Analysis-Tool
   ```

2. Create a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

### Required Dependencies

```
pandas>=1.3.0
numpy>=1.21.0
transformers>=4.30.0
torch>=1.10.0
scikit-learn>=1.0.0
nltk>=3.6.0
spacy>=3.0.0
beautifulsoup4>=4.10.0
PyMuPDF>=1.18.0
wordcloud>=1.8.0
matplotlib>=3.4.0
seaborn>=0.11.0
kneed>=0.8.0
```

---

## Quick Start

1. Run the main notebook

   ```bash
   jupyter notebook notebooks/thematic-analysis-tool.ipynb
   ```

2. Upload your data

   * A PDF document (e.g., research paper or transcript)
   * A web URL list for scraping
   * A plain text file containing paragraphs

3. Execute the pipeline

   ```python
   from src.preprocessing import preprocess_text
   from src.clustering import generate_themes
   from src.sentiment_analysis import analyze_sentiment

   clean_text = preprocess_text("docs/sample_text.pdf")
   themes = generate_themes(clean_text, num_clusters=5)
   sentiments = analyze_sentiment(themes)
   ```

4. Export results

   ```python
   import pandas as pd
   themes.to_csv('results/themes_output.csv', index=False)
   ```

---

## Data Requirements

### Supported Formats

| File Type    | Description                   | Example                      |
| ------------ | ----------------------------- | ---------------------------- |
| **.pdf**     | Research papers or reports    | `data/literature_review.pdf` |
| **.txt**     | Clean text files              | `data/interview_data.txt`    |
| **URL List** | Web links in `.csv` or `.txt` | `data/urls.csv`              |

### Sample Input Format

```
Objective: Analyze employee adaptability to digital transformation
Source: Journal articles and reports (PDF and web)
```

---

## Methodology

### 1. Data Extraction

* Extracts content from PDFs using PyMuPDF
* Cleans web content with BeautifulSoup

### 2. Preprocessing

* Lowercasing, stopword removal, and lemmatization
* Sentence segmentation using SpaCy
* Token filtering (keeps nouns, verbs, and adjectives)

### 3. Theme Identification

* Converts sentences into embeddings using Sentence Transformers
* Applies KMeans and elbow method (via Kneed) for clustering
* Labels each cluster as a theme

### 4. Sentiment Analysis

* Uses transformer-based model (`cardiffnlp/twitter-roberta-base-sentiment`)
* Classifies sentiment per cluster and overall dataset

### 5. Visualization

* Word clouds of key terms per theme
* Sentiment distribution bar charts
* Cluster composition plots

---

## Project Structure

```
thematic-analysis-tool/
│
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── notebooks/
│   └── thematic-analysis-tool.ipynb
│
├── src/
│   ├── __init__.py
│   ├── text_extraction.py
│   ├── preprocessing.py
│   ├── clustering.py
│   ├── sentiment_analysis.py
│   ├── visualization.py
│
└── docs/
    ├── project_summary.md
    ├── methods.md
    └── references.md
```

---

## Usage Examples

### Example 1: Simple Theme Extraction

```python
from src.text_extraction import extract_from_pdf
from src.preprocessing import preprocess_text
from src.clustering import generate_themes

text = extract_from_pdf("docs/research_article.pdf")
cleaned = preprocess_text(text)
themes = generate_themes(cleaned)
print(themes.head())
```

### Example 2: Combined Pipeline

```python
from src.utils import thematic_pipeline

results = thematic_pipeline(
    input_file="data/interview_notes.pdf",
    num_clusters=6
)
results.to_csv("results/themes_with_sentiments.csv")
```

---

## Visualization Outputs

| Visualization       | Description                                           |
| ------------------- | ----------------------------------------------------- |
| **Word Cloud**      | Displays frequent keywords per theme                  |
| **Sentiment Chart** | Shows ratio of positive, neutral, and negative themes |
| **Cluster Map**     | Groups semantically similar ideas together            |

Example:

```python
from src.visualization import plot_wordcloud, plot_sentiments
plot_wordcloud(themes)
plot_sentiments(sentiments)
```

---

## Evaluation and Validation

### Metrics

* Silhouette Score for clustering performance
* Sentiment Consistency across related clusters
* Keyword Overlap between themes

### Observations

* Thematic accuracy improves when text is clean and focused
* Combining multiple documents enhances theme reliability

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit and push your changes
4. Submit a pull request

**Guidelines:**

* Follow PEP 8 style
* Add docstrings and comments
* Update documentation when needed

---

## Citation

If you use this tool for your research or paper, please cite:

```bibtex
@misc{thematic_analysis_tool_2025,
  author = {Smatralph},
  title = {NLP Integrated Thematic Analysis Tool for Research},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/smatralph/Thematic-Analysis-Tool}
}
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Smatralph

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction...
```

---

## Acknowledgments

* Hugging Face Transformers for sentiment and embedding models
* Scikit-learn and Kneed for clustering and optimization
* BeautifulSoup4 and PyMuPDF for text extraction
* Matplotlib and Seaborn for data visualization

---

## Contact

* Issues: [GitHub Issues](https://github.com/smatralph/Thematic-Analysis-Tool/issues)
* Email: [r.b.adeagbo@gmail.com](mailto:r.b.adeagbo@gmail.com)

---

If this project helps your research, please consider giving it a star.
