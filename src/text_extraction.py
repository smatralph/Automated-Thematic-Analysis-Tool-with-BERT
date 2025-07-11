import fitz  # PyMuPDF
from bs4 import BeautifulSoup
import requests

def extract_from_pdf(file_path):
    """Extracts text from a PDF file."""
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text("text")
    return text.strip()

def extract_from_url(url):
    """Fetches and cleans text from a given web page URL."""
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        for script in soup(["script", "style"]):
            script.extract()
        return soup.get_text(separator=" ", strip=True)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

def extract_from_urls(file_path):
    """Reads a list of URLs from a file and extracts text from each."""
    texts = []
    with open(file_path, "r") as file:
        urls = file.readlines()
    for url in urls:
        texts.append(extract_from_url(url.strip()))
    return " ".join(texts)
